from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    def visitClassdecl(self,ctx:CSlangParser.ClassdeclContext):
        return ClassDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.memdecl()])

    def visitMemdecl(self,ctx:CSlangParser.MemdeclContext):
        return AttributeDecl(VarDecl(Id(ctx.ID().getText()),self.visit(ctx.cslangtype())))

    def visitCslangtype(self,ctx:CSlangParser.CslangtypeContext):
        return IntType() if ctx.INTTYPE() else VoidType()
        

    
