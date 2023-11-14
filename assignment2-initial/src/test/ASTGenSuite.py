import unittest
from TestUtils import TestAST
from AST import *
# from ..main.CSlang.utils.AST import *

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

    def test_class_declaration(self):
        input = """class A{}"""
        expect = str(Program([ClassDecl(Id("A"), [])]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_class_declaration_with_super(self):
        input = """class B <- A {}"""
        expect = str(Program([ClassDecl(Id("A"),[],Id("B"))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_class_program_main(self):
        input = """
class Program {
func @main():void {
io.@writeInt(Shape.@numOfShape);
}
}
    """
        expect = str(Program([
            ClassDecl(
                Id("Program"),
                [
                    MethodDecl(Id("@main"), [], VoidType(), Block([
                        CallStmt(
                            Id("io"),
                            Id("@writeInt"),
                            [FieldAccess(Id("Shape"), Id("@numOfShape"))]
                        )
                    ]))
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_multiple_class(self):
        input = """
class A {}
class B {}
class C {}
    """
        expect = str(Program([
            ClassDecl(Id("A"), []),
            ClassDecl(Id("B"), []),
            ClassDecl(Id("C"), [])
        ]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_const_declaration(self):
        input = """
class A {
const a: int = 1;
const @b: int = 2;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                AttributeDecl(ConstDecl(Id("@b"), IntType(), IntLiteral(2)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_const_declaration_multiple(self):
        input = """
class A {
const a,b,c: int = 1,2,3;
const @d,@e,@f: int = 4,5,6;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                AttributeDecl(ConstDecl(Id("b"), IntType(), IntLiteral(2))),
                AttributeDecl(ConstDecl(Id("c"), IntType(), IntLiteral(3))),
                AttributeDecl(ConstDecl(Id("@d"), IntType(), IntLiteral(4))),
                AttributeDecl(ConstDecl(Id("@e"), IntType(), IntLiteral(5))),
                AttributeDecl(ConstDecl(Id("@f"), IntType(), IntLiteral(6)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_var_declaration(self):
        input = """
class A {
var a: int;
var @b: int;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), IntType())),
                AttributeDecl(VarDecl(Id("@b"), IntType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_var_declaration_multiple(self):
        input = """
class A {
    var a,b,c: int;
    var @d,@e,@f: string;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), IntType())),
                AttributeDecl(VarDecl(Id("b"), IntType())),
                AttributeDecl(VarDecl(Id("c"), IntType())),
                AttributeDecl(VarDecl(Id("@d"), StringType())),
                AttributeDecl(VarDecl(Id("@e"), StringType())),
                AttributeDecl(VarDecl(Id("@f"), StringType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_var_declaration_with_init(self):
        input = """
class A {
    var a,b,c: int = 1,2,3;
    var @d,@e,@f: float = 4.0,5.0,6.0;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), IntType(), IntLiteral(1))),
                AttributeDecl(VarDecl(Id("b"), IntType(), IntLiteral(2))),
                AttributeDecl(VarDecl(Id("c"), IntType(), IntLiteral(3))),
                AttributeDecl(VarDecl(Id("@d"), FloatType(), FloatLiteral(4.0))),
                AttributeDecl(VarDecl(Id("@e"), FloatType(), FloatLiteral(5.0))),
                AttributeDecl(VarDecl(Id("@f"), FloatType(), FloatLiteral(6.0)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_func_declaration(self):
        input = """
class A {
    func foo(): void {}
    func @bar(): int {}
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([])),
                MethodDecl(Id("@bar"), [], IntType(), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_func_declaration_with_param(self):
        input = """
class A {
    func foo(a: int, b: float): string {}
    func @bar(a: string, b: [5]int): int {}
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), FloatType())
                ], StringType(), Block([])),
                MethodDecl(Id("@bar"), [
                    VarDecl(Id("a"), StringType()),
                    VarDecl(Id("b"), ArrayType(5, IntType()))
                ], IntType(), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_func_declaration_common_param_type(self):
        input = """
class A {
    func foo(a, b, c: int, d, e: float, f: string): void {}
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType()),
                    VarDecl(Id("d"), FloatType()),
                    VarDecl(Id("e"), FloatType()),
                    VarDecl(Id("f"), StringType())
                ], VoidType(), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_func_declaration_constructor(self):
        input = """
class A {
    func constructor (a: int, b: float) {}
}

class B {
    func constructor() {}
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("constructor"), [
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), FloatType())
                ], VoidType(), Block([]))
            ]),
            ClassDecl(Id("B"), [
                MethodDecl(Id("constructor"), [], VoidType(), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_program_comment_line(self):
        input = """
class A {
    // This is a comment
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [])
        ]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_program_comment_block(self):
        input = """
class A {
    /* This is a comment */
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [])
        ]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_identifiers(self):
        input = """
class A {
    var abcd: int;
    var _abc890: int;
    var __0: int;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("abcd"), IntType())),
                AttributeDecl(VarDecl(Id("_abc890"), IntType())),
                AttributeDecl(VarDecl(Id("__0"), IntType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_at_identifiers(self):
        input = """
class A {
    var @abcd: int;
    var @_abc890: int;
    var @a_0_b: int;
    var @000: int;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("@abcd"), IntType())),
                AttributeDecl(VarDecl(Id("@_abc890"), IntType())),
                AttributeDecl(VarDecl(Id("@a_0_b"), IntType())),
                AttributeDecl(VarDecl(Id("@000"), IntType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_integer_literal(self):
        input = """
class A {
    var a: int = 123;
    var b: int = 0;
    var c: int = 1234567890;
    var d: int = 000; // allows leading zeros
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), IntType(), IntLiteral(123))),
                AttributeDecl(VarDecl(Id("b"), IntType(), IntLiteral(0))),
                AttributeDecl(VarDecl(Id("c"), IntType(), IntLiteral(1234567890))),
                AttributeDecl(VarDecl(Id("d"), IntType(), IntLiteral(0)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_float_literal(self):
        input = """
class A {
    var a: float = 123.0;
    var b: float = 0.0;
    var c: float = 1234567890.0;
    var d: float = 1.;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), FloatType(), FloatLiteral(123.0))),
                AttributeDecl(VarDecl(Id("b"), FloatType(), FloatLiteral(0.0))),
                AttributeDecl(VarDecl(Id("c"), FloatType(), FloatLiteral(1234567890.0))),
                AttributeDecl(VarDecl(Id("d"), FloatType(), FloatLiteral(1.0)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_float_literal_exponent(self):
        input = """
class A {
    var a: float = 123.0e-1;
    var b: float = 0.0e+1;
    var c: float = 1234567890.0e1;
    var c: float = 12e8;
    var d: float = 12E+8;
    var e: float = 12E-8;
    var f: float = 0.33E12;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), FloatType(), FloatLiteral(123.0e-1))),
                AttributeDecl(VarDecl(Id("b"), FloatType(), FloatLiteral(0.0e+1))),
                AttributeDecl(VarDecl(Id("c"), FloatType(), FloatLiteral(1234567890.0e1))),
                AttributeDecl(VarDecl(Id("c"), FloatType(), FloatLiteral(12e8))),
                AttributeDecl(VarDecl(Id("d"), FloatType(), FloatLiteral(12e+8))),
                AttributeDecl(VarDecl(Id("e"), FloatType(), FloatLiteral(12e-8))),
                AttributeDecl(VarDecl(Id("f"), FloatType(), FloatLiteral(0.33e12)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_boolean_literal(self):
        input = """
class A {
    var a: bool = true;
    var b: bool = false;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), BoolType(), BooleanLiteral(True))),
                AttributeDecl(VarDecl(Id("b"), BoolType(), BooleanLiteral(False)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_string_literal(self):
        input = """
class A {
    var a: string = "Hello World";
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), StringType(), StringLiteral("Hello World")))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_string_literal_escape(self):
# \b backspace
# \f formfeed
# \r carriage return
# \n newline
# \t horizontal tab
# \" double quote
# \\ backslash
        input = """
class A {
    var a: string = "Hello\\bWorld";
    var b: string = "Hello\\fWorld";
    var c: string = "Hello\\rWorld";
    var d: string = "Hello\\nWorld";
    var e: string = "Hello\\tWorld";
    var f: string = "Hello\\"World";
    var g: string = "Hello\\\World";
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), StringType(), StringLiteral("Hello\\bWorld"))),
                AttributeDecl(VarDecl(Id("b"), StringType(), StringLiteral("Hello\\fWorld"))),
                AttributeDecl(VarDecl(Id("c"), StringType(), StringLiteral("Hello\\rWorld"))),
                AttributeDecl(VarDecl(Id("d"), StringType(), StringLiteral("Hello\\nWorld"))),
                AttributeDecl(VarDecl(Id("e"), StringType(), StringLiteral("Hello\\tWorld"))),
                AttributeDecl(VarDecl(Id("f"), StringType(), StringLiteral("Hello\\\"World"))),
                AttributeDecl(VarDecl(Id("g"), StringType(), StringLiteral("Hello\\\\World")))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_array_literal(self):
        input = """
class A {
    var a: [5]int = [1,2,3,4,5];
    var b: [5]float = [1.0,2.0,3.0,4.0,5e3];
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))),
                AttributeDecl(VarDecl(Id("b"), ArrayType(5, FloatType()), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0), FloatLiteral(4.0), FloatLiteral(5000.0)])))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_boolean_type_operands(self):
        input = """
class A {
    var a: bool = true;
    var b: bool = !x;
    var c: bool = x && y;
    var d: bool = x || y;
    var e: bool = x == y;
    var f: bool = x != y;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), BoolType(), BooleanLiteral(True))),
                AttributeDecl(VarDecl(Id("b"), BoolType(), UnaryOp("!", Id("x")))),
                AttributeDecl(VarDecl(Id("c"), BoolType(), BinaryOp("&&", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("d"), BoolType(), BinaryOp("||", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("e"), BoolType(), BinaryOp("==", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("f"), BoolType(), BinaryOp("!=", Id("x"), Id("y"))))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_integer_type_operands(self):
        input = """
class A {
    var a: int = 1;
    var b: int = x + y;
    var c: int = x - y;
    var d: int = x * y;
    var e: int = x \ y;
    var f: int = x % y;
    var g: bool = x == y;
    var h: bool = x != y;
    var i: bool = x < y;
    var j: bool = x <= y;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), IntType(), IntLiteral(1))),
                AttributeDecl(VarDecl(Id("b"), IntType(), BinaryOp("+", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("c"), IntType(), BinaryOp("-", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("d"), IntType(), BinaryOp("*", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("e"), IntType(), BinaryOp("\\", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("f"), IntType(), BinaryOp("%", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("g"), BoolType(), BinaryOp("==", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("h"), BoolType(), BinaryOp("!=", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("i"), BoolType(), BinaryOp("<", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("j"), BoolType(), BinaryOp("<=", Id("x"), Id("y"))))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_float_type_operands(self):
        input = """
class A {
    var a: float = 1.0;
    var b: float = x + y;
    var c: float = x - y;
    var d: float = x * y;
    var e: float = x / y;
    var f: float = x > y;
    var g: bool = x >= y;
    var h: bool = x < y;
    var i: bool = x <= y;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), FloatType(), FloatLiteral(1.0))),
                AttributeDecl(VarDecl(Id("b"), FloatType(), BinaryOp("+", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("c"), FloatType(), BinaryOp("-", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("d"), FloatType(), BinaryOp("*", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("e"), FloatType(), BinaryOp("/", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("f"), FloatType(), BinaryOp(">", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("g"), BoolType(), BinaryOp(">=", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("h"), BoolType(), BinaryOp("<", Id("x"), Id("y")))),
                AttributeDecl(VarDecl(Id("i"), BoolType(), BinaryOp("<=", Id("x"), Id("y"))))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test_void_type(self):
        input = """
class A {
    func foo(): void {
        var a: string = "Hello" + "World";
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    VarDecl(Id("a"), StringType(), BinaryOp("+", StringLiteral("Hello"), StringLiteral("World")))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_array_type_declaration(self):
        input = """
class A {
    var a: [5]int;
    var b: [123]float;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), ArrayType(5, IntType()))),
                AttributeDecl(VarDecl(Id("b"), ArrayType(123, FloatType())))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_class_type_init(self):
        input = """
class A {
    var a: A = new A();
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), ClassType(Id("A")), NewExpr(Id("A"), [])))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_class_type_init_null(self):
        input = """
class A {
    var a: A = null;
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(VarDecl(Id("a"), ClassType(Id("A")), NullLiteral()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 333))  

    def test_index_operator(self):
        input = """
class A {
    func foo(): int {
        return a[0];
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], IntType(), Block([
                    Return(
                        ArrayCell(Id("a"), IntLiteral(0))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_index_operator_complex(self):
        input = """
class A {
    func foo(): void {
        a[3+x.foo(2)] := a[b[2]] +3;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        ArrayCell(Id("a"), BinaryOp("+", IntLiteral(3), CallExpr(Id("x"), Id("foo"), [IntLiteral(2)]))),
                        BinaryOp("+", ArrayCell(Id("a"), ArrayCell(Id("b"), IntLiteral(2))), IntLiteral(3))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_index_operator_complex2(self):
        input = """
class A {
    func foo(): void {
        x.b[2] := x.m()[3];
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        ArrayCell(FieldAccess(Id("x"), Id("b")), IntLiteral(2)),
                        ArrayCell(CallExpr(Id("x"), Id("m"), []), IntLiteral(3))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_instance_attribute_access(self):
        input = """
class A {
    func foo(): void {
        x.a := 1;
        x.b := y.c.d.e;
        x.c.d.e.f := x.c;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(Id("x"), Id("a")),
                        IntLiteral(1)
                    ),
                    Assign(
                        FieldAccess(Id("x"), Id("b")),
                        FieldAccess(FieldAccess(FieldAccess(Id("y"),Id("c")),Id("d")),Id("e"))
                    ),
                    Assign(
                        FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("x"), Id("c")), Id("d")), Id("e")), Id("f")),
                        FieldAccess(Id("x"), Id("c"))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_instance_attribute_access_expression(self):
        input = """
class A {
    func foo(): void {
        x := a.quz().a;
        y := @buzz().a;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        FieldAccess(
                            CallExpr(
                                Id("a"),
                                Id("quz"),
                                []
                            ),
                            Id("a")
                        )
                    ),
                    Assign(
                        Id("y"),
                        FieldAccess(
                            CallExpr(
                                None,
                                Id("@buzz"),
                                []
                            ),
                            Id("a")
                        )
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_instance_method_invocation(self):
        input = """
class A {
    func foo(): void {
        a.foo();
        a.quz(d, e, f);
        b.buzz().qox(a, b, c);
        a.foo().bar().quz();
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    CallStmt(
                        Id("a"),
                        Id("foo"),
                        []
                    ),
                    CallStmt(
                        Id("a"),
                        Id("quz"),
                        [
                            Id("d"),
                            Id("e"),
                            Id("f")
                        ]
                    ),
                    CallStmt(
                        CallExpr(
                            Id("b"),
                            Id("buzz"),
                            []
                        ),
                        Id("qox"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    ),
                    CallStmt(
                        CallExpr(
                            CallExpr(
                                Id("a"),
                                Id("foo"),
                                []
                            ),
                            Id("bar"),
                            []
                        ),
                        Id("quz"),
                        []
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_static_attribute_access(self):
        input = """
class A {
    func foo(): void {
        A.@numOfShape := A.@numOfShape + 1;
        @numOfShape := @numOfShape + 1;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(Id("A"), Id("@numOfShape")),
                        BinaryOp("+", FieldAccess(Id("A"), Id("@numOfShape")), IntLiteral(1))
                    ),
                    Assign(
                        FieldAccess(None, Id("@numOfShape")),
                        BinaryOp("+", FieldAccess(None, Id("@numOfShape")), IntLiteral(1))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_static_method_invocation(self):
        input = """
class A {
    func foo(): void {
        A.@test();
        @test();
        B.@test(a,b, c);
        @test(a,b,c);
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    CallStmt(
                        Id("A"),
                        Id("@test"),
                        []
                    ),
                    CallStmt(
                        None,
                        Id("@test"),
                        []
                    ),
                    CallStmt(
                        Id("B"),
                        Id("@test"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    ),
                    CallStmt(
                        None,
                        Id("@test"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_object_creation(self):
        input = """
class A {
    func foo(): void {
        var a: A = new A();
        var b: A = new A(a, b, c);
        var c: A = null;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    VarDecl(Id("a"), ClassType(Id("A")), NewExpr(Id("A"), [])),
                    VarDecl(Id("b"), ClassType(Id("A")), NewExpr(Id("A"), [Id("a"), Id("b"), Id("c")])),
                    VarDecl(Id("c"), ClassType(Id("A")), NullLiteral())
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_self(self):
        input = """
class A {
    func foo(): void {
        self.a := 1;
        self.b := self.c;
        self.c := self.d;
        self.invoke();
        self.invoke(a, b, c);
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(SelfLiteral(), Id("a")),
                        IntLiteral(1)
                    ),
                    Assign(
                        FieldAccess(SelfLiteral(), Id("b")),
                        FieldAccess(SelfLiteral(), Id("c"))
                    ),
                    Assign(
                        FieldAccess(SelfLiteral(), Id("c")),
                        FieldAccess(SelfLiteral(), Id("d"))
                    ),
                    CallStmt(
                        SelfLiteral(),
                        Id("invoke"),
                        []
                    ),
                    CallStmt(
                        SelfLiteral(),
                        Id("invoke"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_variable_declaration_statement(self):
        input = """
class A {
    func foo(): void {
        var a: int;
        var a: int = 1;
        var a, b, c: int;
        var a, b, c: int = 1, 2, 3;
        var a, b, c: int = @foo(), @bar(), @quz();
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("a"), IntType(), IntLiteral(1)),
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType()),
                    VarDecl(Id("a"), IntType(), IntLiteral(1)),
                    VarDecl(Id("b"), IntType(), IntLiteral(2)),
                    VarDecl(Id("c"), IntType(), IntLiteral(3)),
                    VarDecl(Id("a"), IntType(), CallExpr(None, Id("@foo"), [])),
                    VarDecl(Id("b"), IntType(), CallExpr(None, Id("@bar"), [])),
                    VarDecl(Id("c"), IntType(), CallExpr(None, Id("@quz"), []))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_const_declaration_statement(self):
        input = """
class A {
    func foo(): void {
        const a: int = 1;
        const a, b, c: int = 1, 2, 3;
        const a, b, c: int = @foo(), @bar(), @quz();
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                    ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                    ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                    ConstDecl(Id("c"), IntType(), IntLiteral(3)),
                    ConstDecl(Id("a"), IntType(), CallExpr(None, Id("@foo"), [])),
                    ConstDecl(Id("b"), IntType(), CallExpr(None, Id("@bar"), [])),
                    ConstDecl(Id("c"), IntType(), CallExpr(None, Id("@quz"), []))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_assignment_statement(self):
        input = """
class A {
    func foo(): void {
        self.aPI := 3.14;
        value := x.foo(5);
        l[3] := value * 2;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(SelfLiteral(), Id("aPI")),
                        FloatLiteral(3.14)
                    ),
                    Assign(
                        Id("value"),
                        CallExpr(
                            Id("x"),
                            Id("foo"),
                            [
                                IntLiteral(5)
                            ]
                        )
                    ),
                    Assign(
                        ArrayCell(Id("l"), IntLiteral(3)),
                        BinaryOp("*", Id("value"), IntLiteral(2))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_if_statement(self):
        input = """
class A {
    func foo(): void {
        if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
        if j > i {j := j - 1;} else {j := j + 1;}
        if j > i {j := j - 1;}
    }
}
    """
    # class If(Stmt):
    # expr:Expr
    # thenStmt:Block
    # preStmt:Block = None # None if there is no pre-statement
    # elseStmt:Block = None # None if there is no else branch
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    If(
                        BinaryOp(">", Id("j"), Id("i")),
                        Block([
                            Assign(
                                Id("j"),
                                BinaryOp("-", Id("j"), IntLiteral(1))
                            )
                        ]),
                        Block([
                            Assign(
                                Id("i"),
                                IntLiteral(0)
                            )
                        ]),
                        Block([
                            Assign(
                                Id("j"),
                                BinaryOp("+", Id("j"), IntLiteral(1))
                            )
                        ]),
                    ),
                    If(
                        BinaryOp(">", Id("j"), Id("i")),
                        Block([
                            Assign(
                                Id("j"),
                                BinaryOp("-", Id("j"), IntLiteral(1))
                            )
                        ]),
                        None,
                        Block([
                            Assign(
                                Id("j"),
                                BinaryOp("+", Id("j"), IntLiteral(1))
                            )
                        ])
                    ),
                    If(
                        BinaryOp(">", Id("j"), Id("i")),
                        Block([
                            Assign(
                                Id("j"),
                                BinaryOp("-", Id("j"), IntLiteral(1))
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_for_statement(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; i := i + 1 {
            io.@writeInt(i);
        }
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    For(
                        Assign(
                            Id("i"),
                            IntLiteral(0)
                        ),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        Assign(
                            Id("i"),
                            BinaryOp("+", Id("i"), IntLiteral(1))
                        ),
                        Block([
                            CallStmt(
                                Id("io"),
                                Id("@writeInt"),
                                [
                                    Id("i")
                                ]
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_break_statement(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; i := i + 1 {
            break;
        }
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    For(
                        Assign(
                            Id("i"),
                            IntLiteral(0)
                        ),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        Assign(
                            Id("i"),
                            BinaryOp("+", Id("i"), IntLiteral(1))
                        ),
                        Block([
                            Break()
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_continue_statement(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; i := i + 1 {
            continue;
        }
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    For(
                        Assign(
                            Id("i"),
                            IntLiteral(0)
                        ),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        Assign(
                            Id("i"),
                            BinaryOp("+", Id("i"), IntLiteral(1))
                        ),
                        Block([
                            Continue()
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_return_statement(self):
        input = """
class A {
    func foo(): void {
        return;
        return 1;
        return 1.0;
        return true;
        return "Hello World";
        return a;
        return @foo();
        return A.b(1,2,3);
        return new A();
        return null;
        return [1,2,3];
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    Return(None),
                    Return(
                        IntLiteral(1)
                    ),
                    Return(
                        FloatLiteral(1.0)
                    ),
                    Return(
                        BooleanLiteral(True)
                    ),
                    Return(
                        StringLiteral("Hello World")
                    ),
                    Return(
                        Id("a")
                    ),
                    Return(
                        CallExpr(
                            None,
                            Id("@foo"),
                            []
                        )
                    ),
                    Return(
                        CallExpr(
                            Id("A"),
                            Id("b"),
                            [
                                IntLiteral(1),
                                IntLiteral(2),
                                IntLiteral(3)
                            ]
                        )
                    ),
                    Return(
                        NewExpr(
                            Id("A"),
                            []
                        )
                    ),
                    Return(
                        NullLiteral()
                    ),
                    Return(
                        ArrayLiteral(
                            [
                                IntLiteral(1),
                                IntLiteral(2),
                                IntLiteral(3)
                            ]
                        )
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_method_invocation_statement(self):
        input = """
class A {
    func foo(): void {
        a.foo();
        a.quz(d, e, f);
        b.buzz().qox(a, b, c);
        a.foo().bar().quz();
        Shape.@getNumOfShape();
        @getNumOfShape();
        @getNumOfShape(a,b,1);
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    CallStmt(
                        Id("a"),
                        Id("foo"),
                        []
                    ),
                    CallStmt(
                        Id("a"),
                        Id("quz"),
                        [
                            Id("d"),
                            Id("e"),
                            Id("f")
                        ]
                    ),
                    CallStmt(
                        CallExpr(
                            Id("b"),
                            Id("buzz"),
                            []
                        ),
                        Id("qox"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    ),
                    CallStmt(
                        CallExpr(
                            CallExpr(
                                Id("a"),
                                Id("foo"),
                                []
                            ),
                            Id("bar"),
                            []
                        ),
                        Id("quz"),
                        []
                    ),
                    CallStmt(
                        Id("Shape"),
                        Id("@getNumOfShape"),
                        []
                    ),
                    CallStmt(
                        None,
                        Id("@getNumOfShape"),
                        []
                    ),
                    CallStmt(
                        None,
                        Id("@getNumOfShape"),
                        [
                            Id("a"),
                            Id("b"),
                            IntLiteral(1)
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_block_statement(self):
        input = """
class A {
    func foo(): void {
        var r, s: int;
        r := 2.0;
        var a, b: [5]int;
        s := r * r * self.myPI;
        a[0] := s;
        var c: B;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    VarDecl(Id("r"), IntType()),
                    VarDecl(Id("s"), IntType()),
                    Assign(
                        Id("r"),
                        FloatLiteral(2.0)
                    ),
                    VarDecl(Id("a"), ArrayType(5, IntType())),
                    VarDecl(Id("b"), ArrayType(5, IntType())),
                    Assign(
                        Id("s"),
                        BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), FieldAccess(SelfLiteral(), Id("myPI")))
                    ),
                    Assign(
                        ArrayCell(Id("a"), IntLiteral(0)),
                        Id("s")
                    ),
                    VarDecl(Id("c"), ClassType(Id("B")))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test_block_statement_empty(self):
        input = """
class A {
    func foo(): void {
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_program_1(self):
        input = """
class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}
    """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                AttributeDecl(VarDecl(Id("x"), IntType(), IntLiteral(65))),
                MethodDecl(Id("@fact"), [VarDecl(Id("n"), IntType())], IntType(), Block([
                    If(
                        BinaryOp("==", Id("n"), IntLiteral(0)),
                        Block([
                            Return(
                                IntLiteral(1)
                            )
                        ]),
                        None,
                        Block([
                            Return(
                                BinaryOp("*", Id("n"), CallExpr(None, Id("@fact"), [BinaryOp("-", Id("n"), IntLiteral(1))]))
                            )
                        ])
                    )
                ])),
                MethodDecl(Id("@inc"), [VarDecl(Id("n"), IntType()), VarDecl(Id("delta"), IntType())], VoidType(), Block([
                    Assign(
                        Id("n"),
                        BinaryOp("+", Id("n"), Id("delta"))
                    ),
                    Return(
                        Id("n")
                    )
                ])),
                MethodDecl(Id("@main"), [], IntType(), Block([
                    VarDecl(Id("delta"), IntType(), CallExpr(None, Id("@fact"), [IntLiteral(3)])),
                    CallStmt(
                        None,
                        Id("@inc"),
                        [
                            FieldAccess(SelfLiteral(), Id("x")),
                            Id("delta")
                        ]
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeInt"),
                        [
                            FieldAccess(SelfLiteral(), Id("x"))
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_complex_multi_classes_complex(self):
        input = """
class Program {
    func @main():int {
        io.@writeString("Hello World");
        return 0;
    }
}

class Shape {
    const numOfShape: int = 0;
    func @getNumOfShape(): int {
        return @numOfShape;
    }
}

class Foo {
    func fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
    }

    func simple():int {
        var a: int = 1;
        return a;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("@main"), [], IntType(), Block([
                    CallStmt(
                        Id("io"),
                        Id("@writeString"),
                        [
                            StringLiteral("Hello World")
                        ]
                    ),
                    Return(
                        IntLiteral(0)
                    )
                ]))
            ]),
            ClassDecl(Id("Shape"), [
                AttributeDecl(ConstDecl(Id("numOfShape"), IntType(), IntLiteral(0))),
                MethodDecl(Id("@getNumOfShape"), [], IntType(), Block([
                    Return(
                        FieldAccess(None, Id("@numOfShape"))
                    )
                ]))
            ]),
            ClassDecl(Id("Foo"), [
                MethodDecl(Id("fact"), [VarDecl(Id("n"), IntType())], IntType(), Block([
                    If(
                        BinaryOp("==", Id("n"), IntLiteral(0)),
                        Block([
                            Return(
                                IntLiteral(1)
                            )
                        ]),
                        None,
                        Block([
                            Return(
                                BinaryOp("*", Id("n"), CallExpr(None, Id("@fact"), [BinaryOp("-", Id("n"), IntLiteral(1))]))
                            )
                        ])
                    )
                ])),
                MethodDecl(Id("simple"), [], IntType(), Block([
                    VarDecl(Id("a"), IntType(), IntLiteral(1)),
                    Return(
                        Id("a")
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_cslang_io(self):
        input = """
class Program {
    func @main():int {
        io.@readInt();
        io.@writeInt(123);
        io.@readFloat();
        io.@writeFloat(123.0);
        io.@readBool();
        io.@writeBool(true);
        io.@readStr();
        io.@writeStr("Some string");
        return 0;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("@main"), [], IntType(), Block([
                    CallStmt(
                        Id("io"),
                        Id("@readInt"),
                        []
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeInt"),
                        [
                            IntLiteral(123)
                        ]
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@readFloat"),
                        []
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeFloat"),
                        [
                            FloatLiteral(123.0)
                        ]
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@readBool"),
                        []
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeBool"),
                        [
                            BooleanLiteral(True)
                        ]
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@readStr"),
                        []
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeStr"),
                        [
                            StringLiteral("Some string")
                        ]
                    ),
                    Return(
                        IntLiteral(0)
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_sample_1(self):
        input = """class main {var a: int;}"""
        expect = str(Program([
            ClassDecl(Id("main"), [
                AttributeDecl(VarDecl(Id("a"), IntType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_sample_2(self):
        input = """class main {var x, y, z: int = 1, 2, 3;}"""
        expect = str(Program([
            ClassDecl(Id("main"), [
                AttributeDecl(VarDecl(Id("x"), IntType(), IntLiteral(1))),
                AttributeDecl(VarDecl(Id("y"), IntType(), IntLiteral(2))),
                AttributeDecl(VarDecl(Id("z"), IntType(), IntLiteral(3)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_sample_3(self):
        input = """class main{ func a(): void {}}"""
        expect = str(Program([
            ClassDecl(Id("main"), [
                MethodDecl(Id("a"), [], VoidType(), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_sample_4(self):
        input = """class main{
func foo  (a: int, b: float):void {}

func @main():void{
     io.printInt(4);
}}"""
        expect = str(Program([
            ClassDecl(Id("main"), [
                MethodDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), FloatType())], VoidType(), Block([])),
                MethodDecl(Id("@main"), [], VoidType(), Block([
                    CallStmt(
                        Id("io"),
                        Id("printInt"),
                        [
                            IntLiteral(4)
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_cslang_basic_types(self):
        input = """
class Program {
    func @main():void {
        var a: int;
        var b: float;
        var c: bool;
        var d: string;
        var f: Circle;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("@main"), [], VoidType(), Block([
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), FloatType()),
                    VarDecl(Id("c"), BoolType()),
                    VarDecl(Id("d"), StringType()),
                    VarDecl(Id("f"), ClassType(Id("Circle")))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_cslang_arraytype(self):
        input = """
class Program {
    func @main(): void {
        
        var e: [5]int;
        var f: [5]float;
        var g: [5]bool;
        var h: [5]string;
        var i: [5]Circle;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("@main"), [], VoidType(), Block([
                    VarDecl(Id("e"), ArrayType(5, IntType())),
                    VarDecl(Id("f"), ArrayType(5, FloatType())),
                    VarDecl(Id("g"), ArrayType(5, BoolType())),
                    VarDecl(Id("h"), ArrayType(5, StringType())),
                    VarDecl(Id("i"), ArrayType(5, ClassType(Id("Circle"))))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_priority_expr(self):
        input = """
class Program {
    var a: int = 1 + (2 * 3);
    var b: int = (1 + 2) * 3;
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                AttributeDecl(VarDecl(Id("a"), IntType(), BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3))))),
                AttributeDecl(VarDecl(Id("b"), IntType(), BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3))))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_new_expr(self):
        input = """
class Program {
    var a: Circle = new Circle();
    var b: Circle = new Circle(a, b, c);
    var c: Circle = new Circle(@foo(), arr[1], 1 + 3);
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                AttributeDecl(VarDecl(Id("a"), ClassType(Id("Circle")), NewExpr(Id("Circle"), []))),
                AttributeDecl(VarDecl(Id("b"), ClassType(Id("Circle")), NewExpr(Id("Circle"), [Id("a"), Id("b"), Id("c")]))),
                AttributeDecl(VarDecl(Id("c"), ClassType(Id("Circle")), NewExpr(Id("Circle"), [CallExpr(None, Id("@foo"), []), ArrayCell(Id("arr"), IntLiteral(1)), BinaryOp("+", IntLiteral(1), IntLiteral(3))])))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_static_access_expr(self):
        input = """
class Program {
    func main(): void {
        A.@numOfShape := A.@numOfShape + 1;
        @numOfShape := @numOfShape + 1;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(Id("A"), Id("@numOfShape")),
                        BinaryOp("+", FieldAccess(Id("A"), Id("@numOfShape")), IntLiteral(1))
                    ),
                    Assign(
                        FieldAccess(None, Id("@numOfShape")),
                        BinaryOp("+", FieldAccess(None, Id("@numOfShape")), IntLiteral(1))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_instance_expr(self):
        input = """
class Program {
    func main(): void {
        A.numOfShape := A.numOfShape + 1;
        x := B[1].numOfShape;
        x := x.y.z.numOfShape;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(Id("A"), Id("numOfShape")),
                        BinaryOp("+", FieldAccess(Id("A"), Id("numOfShape")), IntLiteral(1))
                    ),
                    Assign(
                        Id("x"),
                        FieldAccess(ArrayCell(Id("B"), IntLiteral(1)), Id("numOfShape"))
                    ),
                    Assign(
                        Id("x"),
                        FieldAccess(FieldAccess(FieldAccess(Id("x"), Id("y")), Id("z")), Id("numOfShape"))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_array_cell_expr(self):
        input = """
class Program {
    func main(): void {
        x := arr[a+1];
        x := arr[1];
        x := arr[b.bar()];
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        ArrayCell(Id("arr"), BinaryOp("+", Id("a"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        ArrayCell(Id("arr"), IntLiteral(1))
                    ),
                    Assign(
                        Id("x"),
                        ArrayCell(Id("arr"), CallExpr(Id("b"), Id("bar"), []))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_unary_sub_expr(self):
        input = """
class Program {
    func main(): void {
        x := -(a+1);
        x := -1;
        x := -b.bar();
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        UnaryOp("-", BinaryOp("+", Id("a"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        UnaryOp("-", IntLiteral(1))
                    ),
                    Assign(
                        Id("x"),
                        UnaryOp("-", CallExpr(Id("b"), Id("bar"), []))
                    )
                ]))
            ])
        ]))

    def test_unary_not_expr(self):
        input = """
class Program {
    func main(): void {
        x := !(a+1);
        x := !false;
        x := !b.bar();
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        UnaryOp("!", BinaryOp("+", Id("a"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        UnaryOp("!", BooleanLiteral(False))
                    ),
                    Assign(
                        Id("x"),
                        UnaryOp("!", CallExpr(Id("b"), Id("bar"), []))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_binary_multiplying_expr(self):
        input = """
class Program {
    func main(): void {
        x := a * b;
        x := a / b;
        x := a % b;
        a := a \ b;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("*", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("/", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("%", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("a"),
                        BinaryOp("\\", Id("a"), Id("b"))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_binary_multiplying_expr_complex(self):
        input = """
        class Program {
            func main(): void {
                x := a[0] * b[1];
                x := a.bar(x,y,z) / @foo();
                x := (a+b) % d;
                a := (1*2/3) \ 4;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("*", ArrayCell(Id("a"), IntLiteral(0)), ArrayCell(Id("b"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("/", CallExpr(Id("a"), Id("bar"), [Id("x"), Id("y"), Id("z")]), CallExpr(None, Id("@foo"), []))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("%", BinaryOp("+", Id("a"), Id("b")), Id("d"))
                    ),
                    Assign(
                        Id("a"),
                        BinaryOp("\\", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_binary_adding_expr(self):
        input = """
class Program {
    func main(): void {
        x := a + b;
        x := a - b;
        x := a + b + c;
        x := a - b + c;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("+", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("-", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), Id("c"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("+", BinaryOp("-", Id("a"), Id("b")), Id("c"))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_binary_adding_expr_complex(self):
        input = """
        class Program {
            func main(): void {
                x := a[0] + b[1];
                x := a.bar(x,y,z) - @foo();
                x := (a+b) + d;
                a := (1+2-3) + 4;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("+", ArrayCell(Id("a"), IntLiteral(0)), ArrayCell(Id("b"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("-", CallExpr(Id("a"), Id("bar"), [Id("x"), Id("y"), Id("z")]), CallExpr(None, Id("@foo"), []))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), Id("d"))
                    ),
                    Assign(
                        Id("a"),
                        BinaryOp("+", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_binary_logical_expr(self):
        input = """
class Program {
    func main(): void {
        x := a && b;
        x := a || b;
        x := a && b || c;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("&&", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("||", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("||", BinaryOp("&&", Id("a"), Id("b")), Id("c"))
                    )
                ]))
            ])
        ]))

    def test_binary_logical_expr_complex(self):
        input = """
        class Program {
            func main(): void {
                x := a[0] && b[1];
                x := a.bar(x,y,z) || @foo();
                x := (a+b) && d;
                a := (1&&2||3) && 4;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("&&", ArrayCell(Id("a"), IntLiteral(0)), ArrayCell(Id("b"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("||", CallExpr(Id("a"), Id("bar"), [Id("x"), Id("y"), Id("z")]), CallExpr(None, Id("@foo"), []))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("&&", BinaryOp("+", Id("a"), Id("b")), Id("d"))
                    ),
                    Assign(
                        Id("a"),
                        BinaryOp("&&", BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_binary_relational_expr(self):
        input = """
class Program {
    func main(): void {
        x := a == b;
        x := a != b;
        x := a < b;
        x := a <= b;
        x := a > b;
        x := a >= b;
        x := a == b == c;
        x := a != b == c;
        x := a < b == c;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("==", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("!=", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("<", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("<=", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp(">", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp(">=", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("==", BinaryOp("==", Id("a"), Id("b")), Id("c"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("==", BinaryOp("!=", Id("a"), Id("b")), Id("c"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("==", BinaryOp("<", Id("a"), Id("b")), Id("c"))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_binary_relational_expr_complex(self):
        input = """
        class Program {
            func main(): void {
                x := a[0] == b[1];
                x := a.bar(x,y,z) != @foo();
                x := (a+b) < d;
                a := (1<2<=3) > 4;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("==", ArrayCell(Id("a"), IntLiteral(0)), ArrayCell(Id("b"), IntLiteral(1)))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("!=", CallExpr(Id("a"), Id("bar"), [Id("x"), Id("y"), Id("z")]), CallExpr(None, Id("@foo"), []))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("<", BinaryOp("+", Id("a"), Id("b")), Id("d"))
                    ),
                    Assign(
                        Id("a"),
                        BinaryOp(">", BinaryOp("<=", BinaryOp("<", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test_binary_string_concatenation_expr(self):
        input = """
class Program {
    func main(): void {
        x := a ^ b;
        x := x.foo() ^ y.bar();
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        BinaryOp("^", Id("a"), Id("b"))
                    ),
                    Assign(
                        Id("x"),
                        BinaryOp("^", CallExpr(Id("x"), Id("foo"), []), CallExpr(Id("y"), Id("bar"), []))
                    )
                ]))
            ])
        ]))

    def test_id_expr(self):
        input = """
class Program {
    func main(): void {
        x := y;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        Id("y")
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_self_expr(self):
        input = """
class Program {
    func main(): void {
        x := self;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        SelfLiteral()
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_static_call(self):
        input = """
class Program {
    func main(): void {
        A.@test();
        @test();
        A.@test(a, b, c);
        @test(a, b, c);
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    CallStmt(
                        Id("A"),
                        Id("@test"),
                        []
                    ),
                    CallStmt(
                        None,
                        Id("@test"),
                        []
                    ),
                    CallStmt(
                        Id("A"),
                        Id("@test"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    ),
                    CallStmt(
                        None,
                        Id("@test"),
                        [
                            Id("a"),
                            Id("b"),
                            Id("c")
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_instance_call(self):
        input = """
class Program {
    func main(): void {
        x := A.test();
        x := A.test(a, b, c);
        x := arr[a+1].test();
        x := arr[a+1].test(a, b.bar(), c + 1);
        x := (a+b).test();
        x := A.b.test();
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        CallExpr(
                            Id("A"),
                            Id("test"),
                            []
                        )
                    ),
                    Assign(
                        Id("x"),
                        CallExpr(
                            Id("A"),
                            Id("test"),
                            [
                                Id("a"),
                                Id("b"),
                                Id("c")
                            ]
                        )
                    ),
                    Assign(
                        Id("x"),
                        CallExpr(
                            ArrayCell(Id("arr"), BinaryOp("+", Id("a"), IntLiteral(1))),
                            Id("test"),
                            []
                        )
                    ),
                    Assign(
                        Id("x"),
                        CallExpr(
                            ArrayCell(Id("arr"), BinaryOp("+", Id("a"), IntLiteral(1))),
                            Id("test"),
                            [
                                Id("a"),
                                CallExpr(
                                    Id("b"),
                                    Id("bar"),
                                    []
                                ),
                                BinaryOp("+", Id("c"), IntLiteral(1))
                            ]
                        )
                    ),
                    Assign(
                        Id("x"),
                        CallExpr(
                            BinaryOp("+", Id("a"), Id("b")),
                            Id("test"),
                            []
                        )
                    ),
                    Assign(
                        Id("x"),
                        CallExpr(
                            FieldAccess(Id("A"), Id("b")),
                            Id("test"),
                            []
                        )                    
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_complex_assignment_stmt(self):
        input = """
class Program {
    func main(): void {
        l[y.x(foo, @bar(a, 2), 3) + t.test()] := (1 + foo.bar() + @quz()) * 3;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        ArrayCell(Id("l"), BinaryOp(
                            "+", 
                            CallExpr(Id("y"), Id("x"), [
                                Id("foo"),
                                CallExpr(None, Id("@bar"), [Id("a"), IntLiteral(2)]),
                                IntLiteral(3)
                            ]),
                            CallExpr(Id("t"), Id("test"), [])
                        )),
                        BinaryOp("*", 
                            BinaryOp(
                                "+",
                                BinaryOp(
                                    "+",
                                    IntLiteral(1),
                                    CallExpr(Id("foo"), Id("bar"), [])
                                ),
                                CallExpr(None, Id("@quz"), [])
                            ),
                            IntLiteral(3)
                        )

                    ),
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_complex_assignment_stmt_2(self):
        input = """
class Program {
    func main(): void {
                self.foo.bar.quz := -(1 * test.foo.bar.quz);
        @foo := 24 * 2;
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        FieldAccess(FieldAccess(FieldAccess(SelfLiteral(), Id("foo")), Id("bar")), Id("quz")),
                        UnaryOp(
                            "-", 
                            BinaryOp(
                                "*", 
                                IntLiteral(1), 
                                FieldAccess(FieldAccess(FieldAccess(Id("test"), Id("foo")), Id("bar")), Id("quz"))
                            )
                        )
                    ),
                    Assign(
                        FieldAccess(None, Id("@foo")),
                        BinaryOp("*", IntLiteral(24), IntLiteral(2))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_const_declaration_statement_2(self):
        input = """
class A {
    func main(): void {
        const a: int = 1;
        const @b: int = 2;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                    ConstDecl(Id("@b"), IntType(), IntLiteral(2))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_const_declaration_multiple_statement_2(self):
        input = """
class A {
    func main(): void {
        const a,b,c: int = 1,2,3;
        const @d,@e,@f: int = 4,5,6;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                    ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                    ConstDecl(Id("c"), IntType(), IntLiteral(3)),
                    ConstDecl(Id("@d"), IntType(), IntLiteral(4)),
                    ConstDecl(Id("@e"), IntType(), IntLiteral(5)),
                    ConstDecl(Id("@f"), IntType(), IntLiteral(6))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 387))


    def test_var_declaration_statement_2(self):
        input = """
class A {
    func main(): void {
        var a: int;
        var @b: int;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("@b"), IntType())
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_var_declaration_multiple_statement_2(self):
        input = """
class A {
    func main(): void {
        var a,b,c: int;
        var @d,@e,@f: string;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType()),
                    VarDecl(Id("@d"), StringType()),
                    VarDecl(Id("@e"), StringType()),
                    VarDecl(Id("@f"), StringType())
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_var_declaration_with_init_statement_2(self):
        input = """
class A {
    func main(): void {
        var a,b,c: int = 1,2,3;
        var @d,@e,@f: float = 4.0,5.0,6.0;
    }
}
    """
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    VarDecl(Id("a"), IntType(), IntLiteral(1)),
                    VarDecl(Id("b"), IntType(), IntLiteral(2)),
                    VarDecl(Id("c"), IntType(), IntLiteral(3)),
                    VarDecl(Id("@d"), FloatType(), FloatLiteral(4.0)),
                    VarDecl(Id("@e"), FloatType(), FloatLiteral(5.0)),
                    VarDecl(Id("@f"), FloatType(), FloatLiteral(6.0))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_var_declaration_with_init_statement_complex(self):
        input = """
class A {
    func main(): void {
        var a: int = arr[0] * (test.foo() + @bar());
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    VarDecl(Id("a"), IntType(), BinaryOp("*", ArrayCell(Id("arr"), IntLiteral(0)), BinaryOp("+", CallExpr(Id("test"), Id("foo"), []), CallExpr(None, Id("@bar"), []))))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_for_statement_complex(self):
        input = """
class A {
    func foo(): void {
        for @foo(); @bar(); @quz() {
            io.@writeInt(i);
        }

        for i := foo.init(); i < x.len() - 5; i := i + 1 {
            io.@writeInt(i);
        }
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], VoidType(), Block([
                    For(
                        CallStmt(None, Id("@foo"), []),
                        CallExpr(None, Id("@bar"), []),
                        CallStmt(None, Id("@quz"), []),
                        Block([
                            CallStmt(
                                Id("io"),
                                Id("@writeInt"),
                                [
                                    Id("i")
                                ]
                            )
                        ])
                    ),
                    For(
                        Assign(Id("i"), CallExpr(Id("foo"), Id("init"), [])),
                        BinaryOp("<", Id("i"), BinaryOp("-", CallExpr(Id("x"), Id("len"), []), IntLiteral(5))),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            CallStmt(
                                Id("io"),
                                Id("@writeInt"),
                                [
                                    Id("i")
                                ]
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_complex_return_statement(self):
        input = """
class A {
    func foo(): int {
        return 1 + 2 * 3;
    }

    func bar(): int {
        return foo.bar();
    }

    func main(): void {
        return @foo * (arr[5].test() + foo.bar());
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Id("foo"), [], IntType(), Block([
                    Return(
                        BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3)))
                    )
                ])),
                MethodDecl(Id("bar"), [], IntType(), Block([
                    Return(
                        CallExpr(Id("foo"), Id("bar"), [])
                    )
                ])),
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Return(
                        BinaryOp("*", 
                            FieldAccess(None, Id("@foo")),
                            BinaryOp(
                                "+",
                                CallExpr(ArrayCell(Id("arr"), IntLiteral(5)), Id("test"), []),
                                CallExpr(Id("foo"), Id("bar"), [])
                            )
                        )
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 393))

    
    def test_program_2(self):
        input = """
class Program {
    func main(): void {
        io.@writeString("Enter the number of shapes: ");
        io.@readInt(@numOfShape);
        @numOfShape := @numOfShape + 1;
        io.@writeString("Number of shapes is: " ^ @numOfShape);
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    CallStmt(
                        Id("io"),
                        Id("@writeString"),
                        [
                            StringLiteral("Enter the number of shapes: ")
                        ]
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@readInt"),
                        [
                            FieldAccess(None, Id("@numOfShape"))
                        ]
                    ),
                    Assign(
                        FieldAccess(None, Id("@numOfShape")),
                        BinaryOp("+", FieldAccess(None, Id("@numOfShape")), IntLiteral(1))
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeString"),
                        [
                            BinaryOp("^", StringLiteral("Number of shapes is: "), FieldAccess(None, Id("@numOfShape")))
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_function_return_type(self):
        input = """
class Program {
    func intfunction(): int {
    }
    func floatfunction(): float {
    }
    func stringfunction(): string {
    }
    func boolfunction(): bool {
    }
    func voidfunction(): void {
    }
    func arrayfunction(): [5]int {
    }
    func objectfunction(): A {
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("intfunction"), [], IntType(), Block([])),
                MethodDecl(Id("floatfunction"), [], FloatType(), Block([])),
                MethodDecl(Id("stringfunction"), [], StringType(), Block([])),
                MethodDecl(Id("boolfunction"), [], BoolType(), Block([])),
                MethodDecl(Id("voidfunction"), [], VoidType(), Block([])),
                MethodDecl(Id("arrayfunction"), [], ArrayType(5, IntType()), Block([])),
                MethodDecl(Id("objectfunction"), [], ClassType(Id("A")), Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_array_assignment_complex(self):
        input = """
class Program {
    func main(): void {
        arr[1][2][3] := 1;
        arr[1][2][3] := 1.0;
        arr[1][2][3] := "string";
        arr[1][2][3] := true;
        arr[1][2][3] := arr[1][2][3];
        arr[1][2][3] := arr[1][2][3].foo();
        arr[1][2][3] := arr[1][2][3].foo(1,2,3);
        arr[1][2][3] := arr[1][2][3].foo(1,2,3).bar();
        arr[1][2][3] := arr[1][2][3].foo(1,2,3).bar(1,2,3);
        arr[1][2][3] := arr[1][2][3].foo(1,2,3).bar(1,2,3).quz();
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        IntLiteral(1)
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        FloatLiteral(1.0)
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        StringLiteral("string")
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        BooleanLiteral(True)
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3))
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        CallExpr(ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)), Id("foo"), [])
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        CallExpr(ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)), Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        CallExpr(CallExpr(ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)), Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Id("bar"), [])
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        CallExpr(CallExpr(ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)), Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Id("bar"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])
                    ),
                    Assign(
                        ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)),
                        CallExpr(CallExpr(CallExpr(ArrayCell(ArrayCell(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)), Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Id("bar"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Id("quz"), [])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_complex_new_expr(self):
        input = """
class Program {
    func main(): void {
        x := new Foo(
            arr[4],
            new Bar(),
            3
        );
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        NewExpr(
                            Id("Foo"),
                            [
                                ArrayCell(Id("arr"), IntLiteral(4)),
                                NewExpr(Id("Bar"), []),
                                IntLiteral(3)
                            ]
                        )
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_complex_new_expr_2(self):
        input = """
class Program {
    func main(): void {
        x := new Foo(
            arr[4],
            new Bar(
                new Quz(),
                3
            ),
            3
        );
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("main"), [], VoidType(), Block([
                    Assign(
                        Id("x"),
                        NewExpr(
                            Id("Foo"),
                            [
                                ArrayCell(Id("arr"), IntLiteral(4)),
                                NewExpr(
                                    Id("Bar"),
                                    [
                                        NewExpr(Id("Quz"), []),
                                        IntLiteral(3)
                                    ]
                                ),
                                IntLiteral(3)
                            ]
                        )
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_program_3(self):
        input = """
class Program {
    func constructor() {
        io.@writeString("Enter the number of shapes: ");
        io.@readInt(@numOfShape);
        @numOfShape := @numOfShape + 1;
        io.@writeString("Number of shapes is: " ^ @numOfShape);
    }
}
"""
        expect = str(Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Id("constructor"), [], None, Block([
                    CallStmt(
                        Id("io"),
                        Id("@writeString"),
                        [
                            StringLiteral("Enter the number of shapes: ")
                        ]
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@readInt"),
                        [
                            FieldAccess(None, Id("@numOfShape"))
                        ]
                    ),
                    Assign(
                        FieldAccess(None, Id("@numOfShape")),
                        BinaryOp("+", FieldAccess(None, Id("@numOfShape")), IntLiteral(1))
                    ),
                    CallStmt(
                        Id("io"),
                        Id("@writeString"),
                        [
                            BinaryOp("^", StringLiteral("Number of shapes is: "), FieldAccess(None, Id("@numOfShape")))
                        ]
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 399))
        