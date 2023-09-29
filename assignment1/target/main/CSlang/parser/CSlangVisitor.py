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


    # Visit a parse tree produced by CSlangParser#attribute.
    def visitAttribute(self, ctx:CSlangParser.AttributeContext):
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


    # Visit a parse tree produced by CSlangParser#data_type.
    def visitData_type(self, ctx:CSlangParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_string.
    def visitExpr_string(self, ctx:CSlangParser.Expr_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_rela.
    def visitExpr_rela(self, ctx:CSlangParser.Expr_relaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_logic.
    def visitExpr_logic(self, ctx:CSlangParser.Expr_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_add.
    def visitExpr_add(self, ctx:CSlangParser.Expr_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_multi.
    def visitExpr_multi(self, ctx:CSlangParser.Expr_multiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_logic_not.
    def visitExpr_logic_not(self, ctx:CSlangParser.Expr_logic_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_sign.
    def visitExpr_sign(self, ctx:CSlangParser.Expr_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_index_op.
    def visitExpr_index_op(self, ctx:CSlangParser.Expr_index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_instance_access.
    def visitExpr_instance_access(self, ctx:CSlangParser.Expr_instance_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_static_access.
    def visitExpr_static_access(self, ctx:CSlangParser.Expr_static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_object_creation.
    def visitExpr_object_creation(self, ctx:CSlangParser.Expr_object_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_term.
    def visitExpr_term(self, ctx:CSlangParser.Expr_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#dcl_stmt.
    def visitDcl_stmt(self, ctx:CSlangParser.Dcl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_stmt.
    def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
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


    # Visit a parse tree produced by CSlangParser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:CSlangParser.Method_invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#element_type.
    def visitElement_type(self, ctx:CSlangParser.Element_typeContext):
        return self.visitChildren(ctx)



del CSlangParser