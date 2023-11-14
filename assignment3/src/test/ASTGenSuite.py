import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_initial(self):
        input = """class main {var x, y, z: int = 1, 2, 3;}"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("x"),IntType(),IntLiteral(1))),
            AttributeDecl(VarDecl(Id("y"),IntType(),IntLiteral(2))),
            AttributeDecl(VarDecl(Id("z"),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_class_with_parent(self):
        input = """class object<-main{ const x, y, z: int = 1, 2, 3;
        var a, b: float;}"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(ConstDecl(Id("x"),IntType(),IntLiteral(1))),
            AttributeDecl(ConstDecl(Id("y"),IntType(),IntLiteral(2))),
            AttributeDecl(ConstDecl(Id("z"),IntType(),IntLiteral(3))),
            AttributeDecl(VarDecl(Id("a"),FloatType())),
            AttributeDecl(VarDecl(Id("b"),FloatType()))],
            Id("object"))]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_class_with_simple_function(self):
        input = """class main{ func a(): void {}}"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Id("a"),[],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_with_many_function(self):
        input = """class main{
func foo  (a: int, b: float):void {}

func @main():void{
     io.printInt(4);
}}"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_with_example_in_spec(self):
        input = """
        class Shape {
        var @numOfShape: int = 0;
        const immutableAttribute: int = 0;
        var length, width: int;
        
        func @getNumOfShape():int {
            return @numOfShape / 1 + 0;
        }
    }
    
    class Shape <- Retangle {
        func getArea():int {
            return self.length * self.width;
        }
    }
    
    class Program {
        func @main():void {
            io.@writeInt(Shape.@numOfShape);
        }
    }
        """
        expect ="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(BinaryOp(+,BinaryOp(/,FieldAccess(Id(@numOfShape)),IntLit(1)),IntLit(0)))]))]),ClassDecl(Id(Retangle),Id(Shape),[MethodDecl(Id(getArea),[],IntType,Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(@writeInt),[FieldAccess(Id(Shape),Id(@numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_with_full_statement(self):
        input = """
    class Program {
        func @main():void {
            var a,b:float=3.0,4.e-3;
            var  d:[5]int=[5,3,6,3,1];
            const s:string = "anv";
            const c:int =  5;
            if {b :=  b+1;} b>c {io.@writeInt(d[c]);} else {io.@writeInt(b);}
            var i:int;
            for i:= 1;i<5;i := i+1 {a := a +1;  b:=b*2; if a <=b {break;} else {continue;}}
            io.@writeStr(s^"anv");
            return;
        }
    }
        """
        expect ="Program([ClassDecl(Id(Program),[MethodDecl(Id(@main),[],VoidType,Block([VarDecl(Id(a),FloatType,FloatLit(3.0)),VarDecl(Id(b),FloatType,FloatLit(0.004)),VarDecl(Id(d),ArrayType(5,IntType),[IntLit(5),IntLit(3),IntLit(6),IntLit(3),IntLit(1)]),ConstDecl(Id(s),StringType,StringLit(anv)),ConstDecl(Id(c),IntType,IntLit(5)),If(Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))]),BinaryOp(>,Id(b),Id(c)),Block([Call(Id(io),Id(@writeInt),[ArrayCell(Id(d),Id(c))])]),Block([Call(Id(io),Id(@writeInt),[Id(b)])])),VarDecl(i,IntType),For(AssignStmt(Id(i),IntLit(1)),BinaryOp(<,Id(i),IntLit(5)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),AssignStmt(Id(b),BinaryOp(*,Id(b),IntLit(2))),If(BinaryOp(<=,Id(a),Id(b)),Block([Break]),Block([Continue]))])]),Call(Id(io),Id(@writeStr),[BinaryOp(^,Id(s),StringLit(anv))]),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,308))

   