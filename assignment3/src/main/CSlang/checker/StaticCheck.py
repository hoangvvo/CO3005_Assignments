"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy


class Member:
    def __init__(self, n: str, t: Type, isMu=False):
        self.name = n
        self.typ = t
        self.isMu = isMu

    def __str__(self):
        return "Member(" + self.name + "," + str(self.typ) + "," + str(self.isMu) + ")"


class BKClass(Utils):
    def __init__(self, n: str, p, m, c=None):
        self.name = n
        self.parent = p
        self.member = m
        self.constructors = c

    def __str__(self):
        return (
            "Class("
            + self.name
            + ","
            + (
                self.parent
                if type(self.parent) == str
                else "None"
                if self.parent is None
                else self.parent.name
            )
            + ",["
            + ",".join(str(i) for i in self.member)
            + "])"
        )

    def get_constructors(self):
        if self.constructors is None:
            return []
        return self.constructors

    def get_member(self, name: str, env):
        for x in self.member:
            if x.name == name:
                return x
        if self.parent is not None:
            parent_class = self.lookup(self.parent.name, env, lambda x: x.name)
            return parent_class.get_member(name, env)
        return None

    def is_current_or_ancestor(self, classname, env):
        if self.name == classname:
            return True
        if self.parent is None:
            return False
        if self.parent.name == classname:
            return True
        parent_class = self.lookup(self.parent.name, env, lambda x: x.name)
        return parent_class.is_current_or_ancestor(classname, env)


class GetEnv(BaseVisitor, Utils):
    def visitProgram(self, ast: Program, c):
        return reduce(lambda a, e: self.visit(e, a), ast.decl, c)

    def visitClassDecl(self, ast: ClassDecl, c):
        if ast.classname.name in map(lambda x: x.name, c):
            # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
            raise Redeclared(Class(), ast.classname.name)

        mem = reduce(lambda a, e: self.visit(e, a), ast.memlist, [])

        memlist = []
        constructors = []
        for x in mem:
            if type(x.typ) is MType and x.name == "constructor":
                constructors.append(x)
            else:
                memlist.append(x)

        return [BKClass(ast.classname.name, ast.parentname, memlist, constructors)] + c

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        field: Member = self.visit(ast.decl, c)
        if field.typ is VoidType:
            # 2.6 Type Mismatch In Declaration
            # The type of a variable, constant, parameter or attribute cannot be void
            raise TypeMismatchInDeclaration(ast)
        return [field] + c

    def visitVarDecl(self, ast: VarDecl, c):
        if ast.variable.name in map(lambda x: x.name, c):
            # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
            raise Redeclared(Attribute(), ast.variable.name)

        return Member(ast.variable.name, ast.varType, True)

    def visitConstDecl(self, ast: ConstDecl, c):
        if ast.constant.name in map(lambda x: x.name, c):
            # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
            raise Redeclared(Attribute(), ast.constant.name)

        return Member(ast.constant.name, ast.constType, False)

    def visitMethodDecl(self, ast: MethodDecl, c):
        if ast.name.name in map(lambda x: x.name, c):
            # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
            raise Redeclared(Method(), ast.name.name)

        params = []
        for x in ast.param:
            if x.variable.name in map(lambda x: x.variable.name, params):
                # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
                raise Redeclared(Parameter(), x.variable.name)

            if x.varType is VoidType:
                # 2.6 Type Mismatch In Declaration
                # The type of a variable, constant, parameter or attribute cannot be void
                raise TypeMismatchInDeclaration(x)

            params.append(x)

        field = Member(
            ast.name.name,
            MType(
                list(map(lambda x: x.varType, ast.param)),
                ast.returnType,
            ),
            False,
        )
        return [field] + c


class Scope(Utils):
    def __init__(self, is_loop=False, classname=None, rettype=None):
        self.var = {}
        self.const = {}
        self.is_loop = is_loop
        self.classname = classname
        self.rettype = rettype

    def add(self, name, typ, is_const=False):
        if is_const:
            self.const[name] = typ
        self.var[name] = typ

    def get(self, name):
        varGet = self.var.get(name, None)
        if varGet is not None:
            return (varGet, False)
        constGet = self.const.get(name, None)
        if constGet is not None:
            return (constGet, True)
        return None


class ScopeStack(Utils):
    def __init__(self):
        # global scope
        self.stack = [Scope()]

    def enter_scope(self, is_loop=False, classname=None, rettype=None):
        self.stack.append(Scope(is_loop=is_loop, classname=classname, rettype=rettype))

    def exit_scope(self):
        self.stack.pop()

    def add_to_scope(self, name: str, typ: Type, is_const: bool):
        self.stack[-1].add(name, typ, is_const)

    def find_in_scope(self, name) -> (Type, bool):
        return self.stack[-1].get(name)

    def is_in_loop(self):
        # return self.stack[-1].isLoop
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].isLoop:
                return True
        return False

    def find_in_all_scope(self, name) -> (Type, bool):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].get(name) is not None:
                return self.stack[i].get(name)
        return None

    def get_current_classname(self):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].classname is not None:
                return self.stack[i].classname
        return None

    def get_current_rettype(self):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].rettype is not None:
                return self.stack[i].rettype
        raise Exception("No return type found")


class StaticChecker(BaseVisitor, Utils):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType()

    def __init__(self, ast):
        self.ast = ast
        self.io = [
            BKClass(
                "io",
                None,
                [
                    Member("@readInt", MType([], StaticChecker.inttype), False),
                    Member(
                        "@writeIntLn",
                        MType([StaticChecker.inttype], StaticChecker.voidtype),
                        False,
                    ),
                ],
            )
        ]
        self.scope_stack = ScopeStack()

    def check(self):
        self.visit(self.ast, self.io)
        return "successful"

    def visitProgram(self, ast: Program, c):
        globalEnv = GetEnv().visit(ast, c)

        for e in globalEnv:
            self.scope_stack.add_to_scope(e.name, ClassType(Id(e.name)), True)

        self.__check_entrypoint(globalEnv)

        for x in ast.decl:
            self.visit(x, globalEnv)

    def visitClassDecl(self, ast: ClassDecl, env):
        self.scope_stack.enter_scope()

        if ast.parentname is not None:
            parent_class = self.lookup(ast.parentname.name, env, lambda x: x.name)
            if parent_class is None:
                # 2.2 Undeclared Identifier/Attribute/Method/Class
                raise Undeclared(Class(), ast.parentname.name)

        for x in ast.memlist:
            # this will either visitAttributeDecl or visitMethodDecl
            self.visit(x, env)

        self.scope_stack.exit_scope()

    def visitAttributeDecl(self, ast: AttributeDecl, env):
        self.visit(ast.decl, env)

    def visitMethodDecl(self, ast: MethodDecl, env):
        self.scope_stack.enter_scope(rettype=ast.returnType)

        for x in ast.param:
            self.visit(x, env)

        self.visit(ast.body, env)

        self.scope_stack.exit_scope()

    def visitVarDecl(self, ast: VarDecl, env):
        if self.scope_stack.find_in_scope(ast.variable.name) is not None:
            # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
            raise Redeclared(Variable(), ast.variable.name)

        if type(ast.varType) is VoidType:
            # 2.6 Type Mismatch In Declaration
            # The type of a variable, constant, parameter or attribute cannot be void
            raise TypeMismatchInDeclaration(ast)

        if ast.varInit is not None:
            var_init_type = self.visit(ast.varInit, env)[0]
            if not self.__check_type_compatible(ast.varType, var_init_type, env):
                # 2.6 Type Mismatch In Declaration
                # If there is the initialization expression in a variable/
                # constant/attribute declaration, the
                # type of the declaration and initialization expression must
                # # conform the type rule for an
                # assignment described above.
                raise TypeMismatchInDeclaration(ast)

        self.scope_stack.add_to_scope(ast.variable.name, ast.varType, False)

    def visitConstDecl(self, ast: ConstDecl, env):
        # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
        if self.scope_stack.find_in_scope(ast.constant.name) is not None:
            raise Redeclared(Constant(), ast.constant.name)

        if ast.value is None:
            # 2.6 Type Mismatch In Declaration
            # A constant must be declared with an initialization expression.
            raise TypeMismatchInDeclaration(ast)

        if type(ast.constType) is VoidType:
            # 2.6 Type Mismatch In Declaration
            # The type of a variable, constant, parameter or attribute cannot be void
            raise TypeMismatchInDeclaration(ast)

        value_typ = self.visit(ast.value, env)[0]
        if not self.__check_type_compatible(ast.constType, value_typ, env):
            # 2.6 Type Mismatch In Declaration
            # If there is the initialization expression in a variable/
            # constant/attribute declaration, the
            # type of the declaration and initialization expression must
            # # conform the type rule for an
            # assignment described above.
            raise TypeMismatchInDeclaration(ast)

        self.scope_stack.add_to_scope(ast.constant.name, ast.constType, True)

    def visitIntType(self, ast: IntType, env):
        return (StaticChecker.inttype, True)

    def visitFloatType(self, ast: FloatType, env):
        return (StaticChecker.floattype, True)

    def visitBoolType(self, ast: BoolType, env):
        return (StaticChecker.booltype, True)

    def visitStringType(self, ast: StringType, env):
        return (StaticChecker.stringtype, True)

    def visitVoidType(self, ast: VoidType, env):
        return (StaticChecker.voidtype, True)

    def visitArrayType(self, ast: ArrayType, env):
        return (ast, True)

    def visitClassType(self, ast: ClassType, env):
        return (ast, True)

    def visitBinaryOp(self, ast: BinaryOp, env):
        left = self.visit(ast.left, env)[0]
        right = self.visit(ast.right, env)[0]
        op = ast.op

        # spec 5.1 Arithmetic operators
        if op in ["+", "-", "*"]:
            if type(left) not in [IntType, FloatType] or type(right) not in [
                IntType,
                FloatType,
            ]:
                raise TypeMismatchInExpression(ast)
            if type(left) is FloatType or type(right) is FloatType:
                return (StaticChecker.floattype, True)
            return (StaticChecker.inttype, True)
        # spec 5.1 Arithmetic operators
        elif op == "/":
            if type(left) not in [IntType, FloatType] or type(right) not in [
                IntType,
                FloatType,
            ]:
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.floattype, True)
        elif op == "\\":
            if type(left) is not IntType or type(right) is not IntType:
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.inttype, True)
        elif op in ["%"]:
            if type(left) is not IntType or type(right) is not IntType:
                raise TypeMismatchInExpression(ast)

            return (StaticChecker.inttype, True)

        # spec 5.2 Boolean operators
        elif op in ["&&", "||"]:
            if type(left) is not BoolType or type(right) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.booltype, True)
        elif op == "^":
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.stringtype, True)
        elif op in ["==", "!="]:
            if type(left) not in [IntType, BoolType] or type(right) not in [
                IntType,
                BoolType,
            ]:
                raise TypeMismatchInExpression(ast)
            if type(left) != type(right):
                # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=15121#p47549
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.booltype, True)
        elif op in ["<", ">", "<=", ">="]:
            if type(left) not in [IntType, FloatType] or type(right) not in [
                IntType,
                FloatType,
            ]:
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.booltype, True)

        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast: UnaryOp, env):
        body = self.visit(ast.body, env)[0]
        op = ast.op

        if op == "-":
            if type(body) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return (body, True)
        elif op == "!":
            if type(body) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return (StaticChecker.booltype, True)

    def visitCallExpr(self, ast: CallExpr, env):
        member: Member = None
        if ast.obj is None:
            # static method call
            # method is of current class
            classname = self.scope_stack.get_current_classname()
            bkclass: BKClass = self.lookup(classname, env, lambda x: x.name)
            member = bkclass.get_member(ast.method.name, env)
        else:
            obj: ClassType = self.visit(ast.obj, env)[0]
            if type(obj) is not ClassType:
                # 2.5 Type Mismatch In Expression
                # For a method call E.<method name>(<args>), E must be in class type;
                raise TypeMismatchInExpression(ast)

            bkclass: BKClass = self.lookup(obj.classname.name, env, lambda x: x.name)
            if bkclass is None:
                # 2.2 Undeclared Identifier/Attribute/Method/Class
                raise Undeclared(Class(), obj.classname.name)

            member = bkclass.get_member(ast.method.name, env)

        if member is None:
            # 2.2 Undeclared Identifier/Attribute/Method/Class
            raise Undeclared(Method(), ast.method.name)

        member_typ: MType = member.typ

        if type(member_typ) is not MType:
            raise TypeMismatchInExpression(ast)

        if type(member_typ.rettype) is VoidType:
            # 2.5 Type Mismatch In Expression
            # the callee <method name> must have non-void as return type
            raise TypeMismatchInExpression(ast)

        if len(member_typ.partype) != len(ast.param):
            # The number of parameters must be equal to that of arguments
            raise TypeMismatchInExpression(ast)

        for i in range(len(member_typ.partype)):
            # the rule for an assignment is applied to parameter passing where
            # a parameter is considered as the LHS and the corresponding argument is the RHS
            typ = self.visit(ast.param[i], env)[0]
            if not self.__check_type_compatible(member_typ.partype[i], typ, env):
                raise TypeMismatchInExpression(ast)

        return (member_typ.rettype, True)

    def visitNewExpr(self, ast: NewExpr, env):
        typ: ClassType = self.scope_stack.find_in_all_scope(ast.classname.name)[0]
        if type(typ) is not ClassType:
            # 2.5 Type Mismatch In Expression
            # For a new expression, the corresponding class
            raise TypeMismatchInExpression(ast)

        bkclass: BKClass = self.lookup(typ.classname.name, env, lambda x: x.name)
        constructors = bkclass.get_constructors()
        if len(constructors) == 0:
            raise TypeMismatchInExpression(ast)

        # the corresponding class must have a constructor method whose
        # number of parameters must be equal to that of arguments and the type of each argument
        # can be coerced to the type of corresponding parameter.
        for constructor in constructors:
            if len(constructor.typ.partype) != len(ast.param):
                continue
            member_typ: MType = constructor.typ
            for i in range(len(member_typ.partype)):
                typ = self.visit(ast.param[i], env)[0]
                if not self.__check_type_compatible(
                    constructor.typ.partype[i], typ, env
                ):
                    continue
            return (typ, True)

        raise TypeMismatchInExpression(ast)

    def visitId(self, ast: Id, env):
        res = self.scope_stack.find_in_all_scope(ast.name)
        if res is None:
            # 2.2 Undeclared Identifier/Attribute/Method/Class
            raise Undeclared(Identifier(), ast.name)
        return res[0], res[1]

    def visitArrayCell(self, ast: ArrayCell, env):
        arr_type: ArrayType = self.visit(ast.arr, env)[0]
        if type(arr_type) != ArrayType:
            # 2.5 Type Mismatch In Expression
            # For an array subcripting E1[E2], E1 must be in array type
            raise TypeMismatchInExpression(ast)

        idx_type = self.visit(ast.idx, env)[0]
        if type(idx_type) != IntType:
            # and E2 must be integer
            raise TypeMismatchInExpression(ast)

        return (arr_type.eleType, False)

    def visitFieldAccess(self, ast: FieldAccess, env):
        member: Member = None
        if ast.obj is None:
            # this is static member access, field name is an "at" identifier
            # static member is of current class
            classname = self.scope_stack.get_current_classname()
            bkclass: BKClass = self.lookup(classname, env, lambda x: x.name)
            member = bkclass.get_member(ast.fieldname.name, env)
        else:
            # ast.obj can be Id or SelfLiteral
            obj = self.visit(ast.obj, env)[0]
            if type(obj) != ClassType:
                # 2.5 Type Mismatch In Expression
                # For an attribute access E.id, E must be in class typ
                raise TypeMismatchInExpression(ast)

            if not ast.fieldname.name.startswith("@"):
                # 2.5 Type Mismatch In Expression
                # e. If id is not "at" identifier, i.e. E.id is an instance field access,
                # the type of E must be the current class or its ancestor.
                current_classname = self.scope_stack.get_current_classname()
                currentbkclass: BKClass = self.lookup(
                    current_classname, env, lambda x: x.name
                )
                if not currentbkclass.is_current_or_ancestor(obj.name, env):
                    raise TypeMismatchInExpression(ast)

            bkclass: BKClass = self.lookup(obj.classname.name, env, lambda x: x.name)
            if bkclass is None:
                # 2.2 Undeclared Identifier/Attribute/Method/Class
                raise Undeclared(Class(), obj.classname.name)
            member = bkclass.get_member(ast.fieldname.name, env)

        if member is None:
            # 2.2 Undeclared Identifier/Attribute/Method/Class
            raise Undeclared(Attribute(), ast.fieldname)

        return (member.typ, not member.isMu)

    def visitBlock(self, ast: Block, env):
        for x in ast.stmt:
            self.visit(x, env)

    def visitIf(self, ast: If, env):
        # FIXME: understand if preStmt scope context
        if ast.preStmt is not None:
            self.visit(ast.preStmt, env)

        cond_type = self.visit(ast.expr, env)[0]
        if type(cond_type) is not BoolType:
            # 2.4 Type Mismatch In Statement
            # The type of a conditional expression in an if or a for statement must be boolean
            raise TypeMismatchInStatement(ast)

        self.scope_stack.enter_scope()
        self.visit(ast.thenStmt, env)
        self.scope_stack.exit_scope()

        if ast.elseStmt is not None:
            self.scope_stack.enter_scope()
            self.visit(ast.elseStmt, env)
            self.scope_stack.exit_scope()

    def visitFor(self, ast: For, env):
        self.visit(ast.initStmt, env)

        cond_type = self.visit(ast.expr, env)[0]
        if type(cond_type) is not BoolType:
            # 2.4 Type Mismatch In Statement
            # The type of a conditional expression in an if or a for statement must be boolean
            raise TypeMismatchInStatement(ast)

        self.visit(ast.postStmt, env)

        self.scope_stack.enter_scope(is_loop=True)
        self.visit(ast.loop, env)
        self.scope_stack.exit_scope()

    def visitContinue(self, ast: Continue, env):
        # 2.7 Break/Continue not in loop
        if not self.scope_stack.is_in_loop():
            raise MustInLoop(ast)

    def visitBreak(self, ast: Break, env):
        # 2.7 Break/Continue not in loop
        if not self.scope_stack.is_in_loop():
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, env):
        current_rettype = self.scope_stack.get_current_rettype()

        if ast.expr is None:
            # 2.4 Type Mismatch In Statement
            # For a return statement, the return expression can be considered
            # as RHS of an implicit assignment whose LHS is the return type.
            if type(current_rettype) is not VoidType:
                raise TypeMismatchInStatement(ast)
            return

        expr_type = self.visit(ast.expr, env)[0]
        if not self.__check_type_compatible(current_rettype, expr_type, env):
            # 2.4 Type Mismatch In Statement
            # For a return statement, the return expression can be considered
            # as RHS of an implicit assignment whose LHS is the return type.
            raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast: Assign, env):
        (lhs_type, is_const) = self.visit(ast.lhs, env)
        if is_const:
            # 2.3 Cannot Assign To Constant
            raise CannotAssignToConstant(ast)

        rhs_type = self.visit(ast.exp, env)[0]
        if not self.__check_type_compatible(lhs_type, rhs_type, env):
            # 2.4 Type Mismatch In Statement
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, env):
        member: Member = None
        if ast.obj is None:
            # static method call
            # method is of current class
            classname = self.scope_stack.get_current_classname()
            bkclass: BKClass = self.lookup(classname, env, lambda x: x.name)
            member = bkclass.get_member(ast.method.name, env)

        else:
            obj: ClassType = self.visit(ast.obj, env)[0]
            if type(obj) is not ClassType:
                # 2.4 Type Mismatch In Statement
                # For a call statement E.<method name>(<args>), E must be in class type;
                raise TypeMismatchInStatement(ast)

            bkclass: BKClass = self.lookup(obj.classname.name, env, lambda x: x.name)
            if bkclass is None:
                # 2.2 Undeclared Identifier/Attribute/Method/Class
                raise Undeclared(Class(), obj.classname.name)

            member = bkclass.get_member(ast.method.name, env)

        if member is None:
            # 2.2 Undeclared Identifier/Attribute/Method/Class
            raise Undeclared(Method(), ast.method.name)

        member_typ: MType = member.typ

        if type(member_typ) is not MType:
            raise TypeMismatchInStatement(ast)

        if type(member_typ.rettype) is not VoidType:
            # 2.4 Type Mismatch In Statement
            # the callee must have void as return type
            raise TypeMismatchInStatement(ast)

        if len(member_typ.partype) != len(ast.param):
            # The number of parameters must be equal to that of arguments
            raise TypeMismatchInStatement(ast)

        for i in range(len(member_typ.partype)):
            # the rule for an assignment is applied to parameter passing where
            # a parameter is considered as the LHS and the corresponding argument is the RHS
            typ = self.visit(ast.param[i], env)[0]
            if not self.__check_type_compatible(member_typ.partype[i], typ, env):
                raise TypeMismatchInStatement(ast)

        return (member_typ.rettype, True)

    def visitIntLiteral(self, ast: IntLiteral, env):
        return (StaticChecker.inttype, True)

    def visitFloatLiteral(self, ast: FloatLiteral, env):
        return (StaticChecker.floattype, True)

    def visitBooleanLiteral(self, ast: BooleanLiteral, env):
        return (StaticChecker.booltype, True)

    def visitStringLiteral(self, ast: StringLiteral, env):
        return (StaticChecker.stringtype, True)

    def visitNullLiteral(self, ast: NullLiteral, env):
        return (ClassType("null"), True)

    def visitSelfLiteral(self, ast: SelfLiteral, env):
        current_classname = self.scope_stack.get_current_classname()
        return (ClassType(Id(current_classname)), True)

    def visitArrayLiteral(self, ast: ArrayLiteral, env):
        elem_typs = list(map(lambda x: self.visit(x, env)[0], ast.value))

        # Illegal Array Literal
        # All literals in an array literal must be in the same type
        if len(elem_typs) > 0:
            elem_typ = elem_typs[0]
            for typ in elem_typs:
                if not self.__check_type_compatible(elem_typ, typ, env):
                    raise IllegalArrayLiteral(ast)

        return (ArrayType(len(ast.value), elem_typ), True)

    def __check_entrypoint(self, env):
        # There must be a function whose name is @main without any parameter and
        # return nothing in the class named Program in a CSlang program.
        program_bkclass: BKClass = self.lookup("Program", env, lambda x: x.name)
        if program_bkclass is None:
            raise NoEntryPoint()

        main_function: Member = program_bkclass.get_member("@main", env)
        if main_function is None:
            raise NoEntryPoint()
        if (
            type(main_function.typ) != MType
            or len(main_function.typ.partype) != 0
            or type(main_function.typ.rettype) != VoidType
        ):
            raise NoEntryPoint()

    def __check_type_compatible(self, lhs_type: Type, rhs_type: Type, env):
        # check coercion (spec - 5.10 Type coercions)

        if type(lhs_type) == type(rhs_type):
            if (type(lhs_type)) == ArrayType:
                # When LHS is in an array type, RHS must be in array type
                # whose size is the same and whose element type can be either the same or able to coerce
                # to the element type of LHS
                if lhs_type.size != rhs_type.size:
                    return False
                return self.__check_type_compatible(
                    lhs_type.eleType, rhs_type.eleType, env
                )

            if isinstance(lhs_type, ClassType):
                if lhs_type.classname.name == rhs_type.classname.name:
                    return True

                if rhs_type.classname.name == "null":
                    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=15120#p47550
                    return True

                rhs_bkclass: BKClass = self.lookup(
                    rhs_type.classname.name, env, lambda x: x.name
                )
                # Note that, as other object-oriented languages, an expression in a subtype can be assigned to a variable in a superclass type without type coercion.
                if not rhs_bkclass.is_current_or_ancestor(lhs_type.classname.name, env):
                    return False

            # If the type of the variable is integer, the expression must be of the type integer.
            # If the type of the variable is boolean, the expression must be of the type boolean.
            return True

        else:
            # If the type of the variable is float, the expression must have either the type integer or float
            if type(lhs_type) == FloatType and (type(rhs_type) in [IntType, FloatType]):
                return True
            return False
