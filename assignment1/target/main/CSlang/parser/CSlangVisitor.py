# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_dcl.
    def visitClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_super.
    def visitClass_super(self, ctx:CSlangParser.Class_superContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_body.
    def visitClass_body(self, ctx:CSlangParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_member.
    def visitClass_member(self, ctx:CSlangParser.Class_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl.
    def visitAttribute_decl(self, ctx:CSlangParser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl_body.
    def visitAttribute_decl_body(self, ctx:CSlangParser.Attribute_decl_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl_inner_without_init.
    def visitAttribute_decl_inner_without_init(self, ctx:CSlangParser.Attribute_decl_inner_without_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl_inner_with_init.
    def visitAttribute_decl_inner_with_init(self, ctx:CSlangParser.Attribute_decl_inner_with_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl_inner_with_init_tail.
    def visitAttribute_decl_inner_with_init_tail(self, ctx:CSlangParser.Attribute_decl_inner_with_init_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_method.
    def visitConstructor_method(self, ctx:CSlangParser.Constructor_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method.
    def visitMethod(self, ctx:CSlangParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param_list.
    def visitParam_list(self, ctx:CSlangParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_lit.
    def visitArray_lit(self, ctx:CSlangParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#data_type.
    def visitData_type(self, ctx:CSlangParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_list.
    def visitExpr_list(self, ctx:CSlangParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#dcl_stmt.
    def visitDcl_stmt(self, ctx:CSlangParser.Dcl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt_body.
    def visitAssign_stmt_body(self, ctx:CSlangParser.Assign_stmt_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_stmt.
    def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_stmt_inner.
    def visitFor_stmt_inner(self, ctx:CSlangParser.For_stmt_innerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_stmt.
    def visitFor_stmt(self, ctx:CSlangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSlangParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSlangParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSlangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_invocation_stmt_body.
    def visitMethod_invocation_stmt_body(self, ctx:CSlangParser.Method_invocation_stmt_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:CSlangParser.Method_invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
        return self.visitChildren(ctx)



del CSlangParser