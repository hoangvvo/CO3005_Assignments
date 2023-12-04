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
    def __init__(self, n, t, isMu=False):
        self.name: str = n
        self.typ: Type = t
        self.isMu: bool = isMu

    def __str__(self):
        return "Member(" + self.name + "," + str(self.typ) + "," + str(self.isMu) + ")"


class BKClass(Utils):
    def __init__(self, n, p, m):
        self.name: str = n
        self.parent = p
        self.member: list(Member) = m

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

    def get_member(self, name: str, env):
        for x in self.member:
            if x.name == name:
                return x
        if self.parent is not None:
            parent_class: BKClass = self.lookup(self.parent.name, env, lambda x: x.name)
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

        return [BKClass(ast.classname.name, ast.parentname, mem)] + c

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        field = self.visit(ast.decl, c)
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
    def __init__(self, isLoop=False, className=None):
        self.var = {}
        self.const = {}
        self.isLoop = isLoop
        self.className = className

    def add(self, name, typ, isConst=False):
        if isConst:
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

    def enter_scope(self, isLoop=False, className=None):
        self.stack.append(Scope(isLoop=isLoop, className=className))

    def exit_scope(self):
        self.stack.pop()

    def add_to_scope(self, name: str, typ: Type, isConst: bool):
        self.stack[-1].add(name, typ, isConst)

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

    def get_current_className(self):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].className is not None:
                return self.stack[i].className
        return None


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

        self.__checkEntryPoint(globalEnv)

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
        self.scope_stack.enter_scope()

        for x in ast.param:
            self.visit(x, env)

        self.visit(ast.body, env)

        self.scope_stack.exit_scope()

    def visitVarDecl(self, ast: VarDecl, env):
        if self.scope_stack.find_in_scope(ast.variable.name) is not None:
            # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
            raise Redeclared(Variable(), ast.variable.name)

        self.scope_stack.add_to_scope(ast.variable.name, ast.varType, False)

    def visitConstDecl(self, ast: ConstDecl, env):
        # 2.1 Redeclared Variable/Constant/Attribute/Class/Method/Parameter
        if self.scope_stack.find_in_scope(ast.constant.name) is not None:
            raise Redeclared(Constant(), ast.constant.name)

        self.scope_stack.add_to_scope(ast.constant.name, ast.constType, True)

    def visitIntType(self, ast: IntType, env):
        return None

    def visitFloatType(self, ast: FloatType, env):
        return None

    def visitBoolType(self, ast: BoolType, env):
        return None

    def visitStringType(self, ast: StringType, env):
        return None

    def visitVoidType(self, ast: VoidType, env):
        return None

    def visitArrayType(self, ast: ArrayType, env):
        return None

    def visitClassType(self, ast: ClassType, env):
        return None

    def visitBinaryOp(self, ast: BinaryOp, env):
        return None

    def visitUnaryOp(self, ast: UnaryOp, env):
        return None

    def visitCallExpr(self, ast: CallExpr, env):
        member: Member = None
        if ast.obj is None:
            # static method call
            # method is of current class
            className = self.scope_stack.get_current_className()
            bkclass: BKClass = self.lookup(className, env, lambda x: x.name)
            member = bkclass.get_member(ast.method.name, env)
        else:
            (obj, isConst) = self.visit(ast.obj, env)
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

        memberTyp: MType = member.typ

        if type(memberTyp) is not MType:
            raise TypeMismatchInExpression(ast)

        if type(memberTyp.rettype) is VoidType:
            # 2.5 Type Mismatch In Expression
            # the callee <method name> must have non-void as return type
            raise TypeMismatchInExpression(ast)

        if len(memberTyp.partype) != len(ast.param):
            # The number of parameters must be equal to that of arguments
            raise TypeMismatchInExpression(ast)

        for i in range(len(memberTyp.partype)):
            # the rule for an assignment is applied to parameter passing where
            # a parameter is considered as the LHS and the corresponding argument is the RHS
            typ = self.visit(ast.param[i], env)[0]
            if not self.__check_type_compatible(memberTyp.partype[i], typ, env):
                raise TypeMismatchInExpression(ast)

        return memberTyp.rettype

    def visitNewExpr(self, ast: NewExpr, env):
        return None

    def visitId(self, ast: Id, env):
        typ, isConst = self.scope_stack.find_in_all_scope(ast.name)
        if typ is None:
            # 2.2 Undeclared Identifier/Attribute/Method/Class
            raise Undeclared(Identifier(), ast.name)
        return typ, isConst

    def visitArrayCell(self, ast: ArrayCell, env):
        return None

    def visitFieldAccess(self, ast: FieldAccess, env):
        member: Member = None
        if ast.obj is None:
            # this is static member access, field name is an "at" identifier
            # static member is of current class
            className = self.scope_stack.get_current_className()
            bkclass: BKClass = self.lookup(className, env, lambda x: x.name)
            member = bkclass.get_member(ast.fieldname.name, env)
        else:
            # ast.obj can be Id or SelfLiteral
            obj = self.visit(ast.obj, env)[0]
            if type(obj) is not ClassType:
                # 2.5 Type Mismatch In Expression
                # For an attribute access E.id, E must be in class typ
                raise TypeMismatchInExpression(ast)

            if not ast.fieldname.name.startswith("@"):
                # 2.5 Type Mismatch In Expression
                # e. If id is not "at" identifier, i.e. E.id is an instance field access,
                # the type of E must be the current class or its ancestor.
                currentClassname = self.scope_stack.get_current_className()
                currentbkclass: BKClass = self.lookup(
                    currentClassname, env, lambda x: x.name
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
        self.visit(ast.expr, env)
        self.scope_stack.enter_scope()
        self.visit(ast.thenStmt, env)
        self.scope_stack.exit_scope()

        if ast.elseStmt is not None:
            self.scope_stack.enter_scope()
            self.visit(ast.elseStmt, env)
            self.scope_stack.exit_scope()

    def visitFor(self, ast: For, env):
        self.visit(ast.initStmt, env)
        self.visit(ast.expr, env)
        self.visit(ast.postStmt, env)

        self.scope_stack.enter_scope(isLoop=True)
        self.visit(ast.loop, env)
        self.scope_stack.exit_scope()

    def visitContinue(self, ast: Continue, env):
        # 2.7 Break/Continue not in loop
        if not self.scope_stack.is_in_loop():
            raise MustInLoop(ast)
        return None

    def visitBreak(self, ast: Break, env):
        # 2.7 Break/Continue not in loop
        if not self.scope_stack.is_in_loop():
            raise MustInLoop(ast)
        return None

    def visitReturn(self, ast: Return, env):
        return None

    def visitAssign(self, ast: Assign, env):
        return None

    def visitCallStmt(self, ast: CallStmt, env):
        return None

    def visitIntLiteral(self, ast: IntLiteral, env):
        return (StaticChecker.inttype, True)

    def visitFloatLiteral(self, ast: FloatLiteral, env):
        return (StaticChecker.floattype, True)

    def visitBooleanLiteral(self, ast: BooleanLiteral, env):
        return (StaticChecker.booltype, True)

    def visitStringLiteral(self, ast: StringLiteral, env):
        return (StaticChecker.stringtype, True)

    def visitNullLiteral(self, ast: NullLiteral, env):
        pass

    def visitSelfLiteral(self, ast: SelfLiteral, env):
        currentClassname = self.scope_stack.get_current_className()
        return (ClassType(Id(currentClassname)), True)

    def visitArrayLiteral(self, ast: ArrayLiteral, env):
        return None

    def __checkEntryPoint(self, env):
        # There must be a function whose name is @main without any parameter and
        # return nothing in the class named Program in a CSlang program.
        programClassMem = self.lookup("Program", env, lambda x: x.name)
        if programClassMem is None:
            raise NoEntryPoint()
        programClassMain = self.lookup(
            "@main", programClassMem.member, lambda x: x.name
        )
        if programClassMain is None:
            raise NoEntryPoint()
        if (
            type(programClassMain.typ) != MType
            or len(programClassMain.typ.partype) != 0
            or type(programClassMain.typ.rettype) != VoidType
        ):
            raise NoEntryPoint()

    def __check_type_compatible(self, lhs_type, rhs_type, env):
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
