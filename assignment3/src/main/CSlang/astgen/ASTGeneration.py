# from .....target.main.CSlang.parser.CSlangVisitor import CSlangVisitor
# from .....target.main.CSlang.parser.CSlangParser import CSlangParser
# from ..utils.AST import *

from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

from functools import reduce


def flatten(lst):
    return reduce(lambda x, y: x + y if type(y) is list else x + [y], lst, [])


class ASTGeneration(CSlangVisitor):
    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx: CSlangParser.ProgramContext) -> Program:
        return Program([self.visit(x) for x in ctx.classdecl()])

    # Visit a parse tree produced by CSlangParser#classdecl.
    def visitClassdecl(self, ctx: CSlangParser.ClassdeclContext) -> ClassDecl:
        return ClassDecl(
            Id(ctx.ID().getText()),
            flatten([self.visit(x) for x in ctx.memdecl()]),
            self.visit(ctx.classsuper()) if ctx.classsuper() else None,
        )

    # Visit a parse tree produced by CSlangParser#classsuper.
    def visitClasssuper(self, ctx: CSlangParser.ClasssuperContext) -> Id:
        return Id(ctx.ID().getText())

    # Visit a parse tree produced by CSlangParser#memdecl.
    def visitMemdecl(self, ctx: CSlangParser.MemdeclContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by CSlangParser#attributedecl.
    def visitAttributedecl(
        self, ctx: CSlangParser.AttributedeclContext
    ) -> List[AttributeDecl]:
        return self.visit(ctx.attributedecl_body())

    # Visit a parse tree produced by CSlangParser#attributedecl_body.
    def visitAttributedecl_body(
        self, ctx: CSlangParser.Attributedecl_bodyContext
    ) -> List[AttributeDecl]:
        attributeDecls = (
            self.visit(ctx.attributedecl_inner_with_init())
            if ctx.attributedecl_inner_with_init()
            else self.visit(ctx.attributedecl_inner_without_init())
        )

        if ctx.CONST():
            return [AttributeDecl(ConstDecl(*args)) for args in attributeDecls]
        else:
            return [AttributeDecl(VarDecl(*args)) for args in attributeDecls]

    # Visit a parse tree produced by CSlangParser#attributedecl_inner_without_init.
    def visitAttributedecl_inner_without_init(
        self, ctx: CSlangParser.Attributedecl_inner_without_initContext
    ):
        # attributedecl_inner_without_init: (AT_ID | ID) (CM (AT_ID | ID))* COLON cslangtype;
        attributeDecls = []

        for i in range(ctx.getChildCount() - 2):
            if i % 2 == 0:
                attributeDecls.append(
                    [Id(ctx.getChild(i).getText()), self.visit(ctx.cslangtype())]
                )

        return attributeDecls

    # Visit a parse tree produced by CSlangParser#attributedecl_inner_with_init.
    def visitAttributedecl_inner_with_init(
        self, ctx: CSlangParser.Attributedecl_inner_with_initContext
    ):
        # attributedecl_inner_with_init: (AT_ID | ID) attributedecl_inner_with_init_tail expr;
        # attributedecl_inner_with_init_tail:
        #     CM (AT_ID | ID) attributedecl_inner_with_init_tail expr CM
        #     | COLON cslangtype ASSIGN_OP;

        #
        idlst = [Id(ctx.AT_ID().getText() if ctx.AT_ID() else ctx.ID().getText())]
        exprlst = [self.visit(ctx.expr())]
        cslangtype = None

        arr = self.visit(ctx.attributedecl_inner_with_init_tail())

        for i in range(len(arr)):
            if len(arr[i]) == 2:
                idlst.append(arr[i][0])
                exprlst.insert(0, arr[i][1])
            else:
                cslangtype = arr[i][0]

        return [[id, cslangtype, expr] for id, expr in zip(idlst, exprlst)]

    # Visit a parse tree produced by CSlangParser#attributedecl_inner_with_init_tail.
    def visitAttributedecl_inner_with_init_tail(
        self, ctx: CSlangParser.Attributedecl_inner_with_init_tailContext
    ):
        if ctx.cslangtype():
            return [[self.visit(ctx.cslangtype())]]
        else:
            return [
                [
                    Id(ctx.AT_ID().getText() if ctx.AT_ID() else ctx.ID().getText()),
                    self.visit(ctx.expr()),
                ]
            ] + self.visit(ctx.attributedecl_inner_with_init_tail())

    # Visit a parse tree produced by CSlangParser#constructormethod.
    def visitConstructormethod(
        self, ctx: CSlangParser.ConstructormethodContext
    ) -> MethodDecl:
        return MethodDecl(
            Id(ctx.CONSTRUCTOR().getText()),
            self.visit(ctx.paramlist()) if ctx.paramlist() else [],
            VoidType(),
            self.visit(ctx.blockstmt()),
        )

    # Visit a parse tree produced by CSlangParser#methoddecl.
    def visitMethoddecl(self, ctx: CSlangParser.MethoddeclContext) -> MethodDecl:
        return MethodDecl(
            Id(ctx.ID().getText() if ctx.ID() else ctx.AT_ID().getText()),
            self.visit(ctx.paramlist()) if ctx.paramlist() else [],
            self.visit(ctx.cslangtype()) if ctx.cslangtype() else VoidType(),
            self.visit(ctx.blockstmt()),
        )

    # Visit a parse tree produced by CSlangParser#paramlist.
    def visitParamlist(self, ctx: CSlangParser.ParamlistContext) -> List[VarDecl]:
        return [y for x in ctx.param() for y in self.visit(x)]

    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx: CSlangParser.ParamContext) -> List[VarDecl]:
        return list(
            map(
                lambda x: VarDecl(Id(x.getText()), self.visit(ctx.cslangtype())),
                ctx.ID(),
            )
        )

    # Visit a parse tree produced by CSlangParser#array_lit.
    def visitArray_lit(self, ctx: CSlangParser.Array_litContext) -> ArrayLiteral:
        return ArrayLiteral([self.visit(x) for x in ctx.lit()])

    # Visit a parse tree produced by CSlangParser#lit.
    def visitLit(self, ctx: CSlangParser.LitContext) -> Literal:
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)

    # Visit a parse tree produced by CSlangParser#cslangtype.
    def visitCslangtype(self, ctx: CSlangParser.CslangtypeContext) -> Type:
        if ctx.BOOLTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())

    # Visit a parse tree produced by CSlangParser#elementtype.
    def visitElementtype(self, ctx: CSlangParser.ElementtypeContext):
        if ctx.BOOLTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))

    # Visit a parse tree produced by CSlangParser#arraytype.
    def visitArraytype(self, ctx: CSlangParser.ArraytypeContext) -> ArrayType:
        return ArrayType(int(ctx.INT_LIT().getText()), self.visit(ctx.elementtype()))

    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx: CSlangParser.ExprContext) -> Expr:
        # expr:
        # 	LB expr RB  # Expr()                                                            # 0. Expr()
        # 	| <assoc = right> NEW ID LB exprlist? RB                                        # 1. NewExpr()
        # 	| (ID DOT)? AT_ID (LB exprlist? RB)?                                            # 2. FieldAccess() or CallExpr()
        # 	| <assoc = left> expr DOT ID (LB exprlist? RB)?                                 # 3. FieldAccess() or CallExpr()
        # 	| expr LS expr RS                                                               # 4. ArrayCell()
        # 	| <assoc = right> SUB_OP expr                                                   # 5. UnaryOp()
        # 	| <assoc = right> NEGATE expr                                                   # 5. UnaryOp()
        # 	| <assoc = left> expr (MUL_OP | DIV_OP | BACKSLASH | MOD_OP) expr               # 6. BinaryOp()
        # 	| <assoc = left> expr (ADD_OP | SUB_OP) expr                                    # 6. BinaryOp()
        # 	| <assoc = left> expr (AND | OR) expr                                           # 6. BinaryOp()
        # 	| expr (
        # 		EQUAL
        # 		| NOT_EQUAL
        # 		| LESS_THAN
        # 		| GREATER_THAN
        # 		| LESS_EQUAL
        # 		| GREATER_EQUAL
        # 	) expr                                                                          # 6. BinaryOp()
        # 	| expr POW_OP expr                                                              # 6. BinaryOp()
        # 	| (
        # 		INT_LIT
        # 		| FLOAT_LIT
        # 		| TRUE
        # 		| FALSE
        # 		| STRING_LIT
        # 		| array_lit
        # 		| NULL
        # 	)                                                                                # 7. Literal()
        # 	| SELF                                                                           # 7. SelfLiteral()
        # 	| ID;                                                                            # 7. Id()
        # exprlist: expr (CM expr)*;
        if ctx.NEW():  # 1. NewExpr()
            return NewExpr(
                Id(ctx.ID().getText()),
                self.visit(ctx.exprlist()) if ctx.exprlist() else [],
            )

        elif ctx.AT_ID():  # 2. FieldAccess() or CallExpr()
            if ctx.LB():
                return CallExpr(
                    Id(ctx.ID().getText()) if ctx.ID() else None,  # (ID DOT)?
                    Id(ctx.AT_ID().getText()),
                    self.visit(ctx.exprlist()) if ctx.exprlist() else [],
                )
            else:
                return FieldAccess(
                    Id(ctx.ID().getText()) if ctx.ID() else None,  # (ID DOT)?
                    Id(ctx.AT_ID().getText()),
                )

        elif ctx.DOT():  # 3. FieldAccess() or CallExpr()
            if ctx.LB():
                return CallExpr(
                    self.visit(ctx.expr(0)),
                    Id(ctx.ID().getText()),
                    self.visit(ctx.exprlist()) if ctx.exprlist() else [],
                )
            else:
                return FieldAccess(self.visit(ctx.expr(0)), Id(ctx.ID().getText()))

        elif ctx.LS():  # 4. ArrayCell()
            return ArrayCell(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

        elif len(ctx.expr()) == 2:  # 6. BinaryOp()
            return BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.expr(0)),
                self.visit(ctx.expr(1)),
            )
        elif ctx.getChildCount() == 1:  # 7.
            if ctx.INT_LIT():
                return IntLiteral(int(ctx.INT_LIT().getText()))
            elif ctx.FLOAT_LIT():
                return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
            elif ctx.STRING_LIT():
                return StringLiteral(ctx.STRING_LIT().getText())
            elif ctx.TRUE():
                return BooleanLiteral(True)
            elif ctx.FALSE():
                return BooleanLiteral(False)
            elif ctx.array_lit():
                return self.visit(ctx.array_lit())
            elif ctx.NULL():
                return NullLiteral()
            elif ctx.SELF():
                return SelfLiteral()
            elif ctx.ID():
                return Id(ctx.ID().getText())
        elif ctx.getChildCount() == 2:  # 5. UnaryOp()
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr(0)))
        else:  # 0. Expr()
            return self.visit(ctx.expr(0))

    # Visit a parse tree produced by CSlangParser#exprlist.
    def visitExprlist(self, ctx: CSlangParser.ExprlistContext) -> List[Expr]:
        return [self.visit(x) for x in ctx.expr()]

    # Visit a parse tree produced by CSlangParser#dclstmt.
    def visitDclstmt(self, ctx: CSlangParser.DclstmtContext):
        attrdecls = self.visitAttributedecl(ctx.attributedecl())
        return [x.decl for x in attrdecls]

    # Visit a parse tree produced by CSlangParser#assignstmt_body.
    def visitAssignstmt_body(self, ctx: CSlangParser.Assignstmt_bodyContext) -> Assign:
        return Assign(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    # Visit a parse tree produced by CSlangParser#assignstmt.
    def visitAssignstmt(self, ctx: CSlangParser.AssignstmtContext) -> Assign:
        return self.visit(ctx.assignstmt_body())

    # Visit a parse tree produced by CSlangParser#ifstmt.
    def visitIfstmt(self, ctx: CSlangParser.IfstmtContext) -> If:
        if ctx.ELSE():
            # either IF blockstmt expr blockstmt ELSE blockstmt;
            # or     IF expr blockstmt ELSE blockstmt;
            if len(ctx.blockstmt()) == 3:
                return If(
                    self.visit(ctx.expr()),
                    self.visit(ctx.blockstmt(1)),
                    self.visit(ctx.blockstmt(0)),
                    self.visit(ctx.blockstmt(2)),
                )
            else:
                return If(
                    self.visit(ctx.expr()),
                    self.visit(ctx.blockstmt(0)),
                    None,
                    self.visit(ctx.blockstmt(1)),
                )
        else:
            # either IF blockstmt expr blockstmt;
            # or     IF expr blockstmt;
            if len(ctx.blockstmt()) == 2:
                return If(
                    self.visit(ctx.expr()),
                    self.visit(ctx.blockstmt(1)),
                    self.visit(ctx.blockstmt(0)),
                    None,
                )
            else:
                return If(self.visit(ctx.expr()), self.visit(ctx.blockstmt(0)))

    # Visit a parse tree produced by CSlangParser#forstmt_inner.
    def visitForstmt_inner(self, ctx: CSlangParser.Forstmt_innerContext) -> For:
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by CSlangParser#forstmt.
    def visitForstmt(self, ctx: CSlangParser.ForstmtContext) -> For:
        return For(
            self.visit(ctx.forstmt_inner(0)),
            self.visit(ctx.expr()),
            self.visit(ctx.forstmt_inner(1)),
            self.visit(ctx.blockstmt()),
        )

    # Visit a parse tree produced by CSlangParser#breakstmt.
    def visitBreakstmt(self, ctx: CSlangParser.BreakstmtContext) -> Break:
        return Break()

    # Visit a parse tree produced by CSlangParser#continuestmt.
    def visitContinuestmt(self, ctx: CSlangParser.ContinuestmtContext) -> Continue:
        return Continue()

    # Visit a parse tree produced by CSlangParser#returnstmt.
    def visitReturnstmt(self, ctx: CSlangParser.ReturnstmtContext) -> Return:
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)

    # Visit a parse tree produced by CSlangParser#methodinvocationstmt_body.
    def visitMethodinvocationstmt_body(
        self, ctx: CSlangParser.Methodinvocationstmt_bodyContext
    ) -> CallStmt:
        if ctx.AT_ID():
            return CallStmt(
                Id(ctx.ID().getText()) if ctx.ID() else None,
                Id(ctx.AT_ID().getText()),
                self.visit(ctx.exprlist()) if ctx.exprlist() else [],
            )
        else:
            return CallStmt(
                self.visit(ctx.expr()),
                Id(ctx.ID().getText()),
                self.visit(ctx.exprlist()) if ctx.exprlist() else [],
            )

    # Visit a parse tree produced by CSlangParser#methodinvocationstmt.
    def visitMethodinvocationstmt(
        self, ctx: CSlangParser.MethodinvocationstmtContext
    ) -> CallStmt:
        return self.visit(ctx.methodinvocationstmt_body())

    # Visit a parse tree produced by CSlangParser#blockstmt.
    def visitBlockstmt(self, ctx: CSlangParser.BlockstmtContext) -> Block:
        if ctx.getChildCount() <= 2:
            return Block([])

        stmts = []

        for i in range(1, ctx.getChildCount() - 1):
            stmts.append(self.visit(ctx.getChild(i)))

        return Block(flatten(stmts))
