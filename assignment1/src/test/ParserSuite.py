import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """class A{var a,b: int = 2,3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_class_declaration(self):
        input = """class A{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_class_declaration_with_super(self):
        input = """class B <- A {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    def test_class_declaration_invalid_name(self):
        input = """class 123 {}"""
        expect = "Error on line 1 col 6: 123"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_class_declaration_invalid_super(self):
        input = """class A <- 123 {}"""
        expect = "Error on line 1 col 11: 123"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_class_declaration_invalid_multiple_super(self):
        input = """class A <- B <- C {}"""
        expect = "Error on line 1 col 13: <-"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_class_program_main(self):
        input = """
class Program {
func @main():void {
io.@writeInt(Shape.@numOfShape);
}
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_multiple_class(self):
        input = """
class A {}
class B {}
class C {}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_const_declaration(self):
        input = """
class A {
const a: int = 1;
const @b: int = 2;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_const_declaration_multiple(self):
        input = """
class A {
const a,b,c: int = 1,2,3;
const @d,@e,@f: int = 4,5,6;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_const_declaration_invalid_mismatch_number(self):
        input = """
class A {
const a,b,c: int = 1,2;
}
    """
        expect = "Error on line 3 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_var_declaration(self):
        input = """
class A {
var a: int;
var @b: int;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_var_declaration_multiple(self):
        input = """
class A {
    var a,b,c: int;
    var @d,@e,@f: string;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_var_declaration_with_init(self):
        input = """
class A {
    var a,b,c: int = 1,2,3;
    var @d,@e,@f: float = 4,5,6;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_var_declaration_invalid_mismatch_number(self):
        input = """
class A {
    var a,b,c: int = 1,2;
}
    """
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_func_declaration(self):
        input = """
class A {
    func foo(): void {}
    func @bar(): int {}
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_func_declaration_with_param(self):
        input = """
class A {
    func foo(a: int, b: float): string {}
    func @bar(a: string, b: [5]int): int {}
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_func_declaration_invalid_param_separator(self):
        input = """
class A {
    func foo(a: int; b: float): string {}
}
    """
        expect = "Error on line 3 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_func_declaration_invalid_param_type(self):
        input = """
class A {
    func foo(a: 000): string {}
}
    """
        expect = "Error on line 3 col 16: 000"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_func_declaration_common_param_type(self):
        input = """
class A {
    func foo(a, b, c: int, d, e: float, f: string): void {}
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_func_declaration_missing_param_type(self):
        input = """
class A {
    func foo(a, b, c, d, e, f): void {}
}
    """
        expect = "Error on line 3 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 220))
    
    def test_func_declaration_missing_return_type(self):
        input = """
class A {
    func foo(): {}
}
    """
        expect = "Error on line 3 col 16: {"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_func_declaration_invalid_return_type(self):
        input = """
class A {
    func foo(): @xd {}
}
    """
        expect = "Error on line 3 col 16: @xd"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_func_declaration_constructor(self):
        input = """
class A {
    func constructor (a: int, b: float) {}
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_func_declaration_constructor_invalid_has_return_type(self):
        input = """
class A {
    func constructor (a: int, b: float): void {}
}
    """
        expect = "Error on line 3 col 39: :"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_program_comment_line(self):
        input = """
class A {
    // This is a comment
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_program_comment_block(self):
        input = """
class A {
    /* This is a comment */
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_identifiers(self):
        input = """
class A {
    var abcd: int;
    var _abc890: int;
    var __0: int;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_at_identifiers(self):
        input = """
class A {
    var @abcd: int;
    var @_abc890: int;
    var @a_0_b: int;
    var @000: int;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_invalid_identifiers(self):
        input = """
class A {
    var 123: int;
}
    """
        expect = "Error on line 3 col 8: 123"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_invalid_identifiers_2(self):
        input = """
class A {
    var !: int;
}
    """
        expect = "Error on line 3 col 8: !"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_invalid_identifer_reserved_keywords(self):
        input = """
class A {
    var return: int;
}
    """
        expect = "Error on line 3 col 8: return"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_integer_literal(self):
        input = """
class A {
    var a: int = 123;
    var b: int = 0;
    var c: int = 1234567890;
    var d: int = 000; // allows leading zeros
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_integer_literal_invalid(self):
        input = """
class A {
    var a: int = 123a;
}
    """
        expect = "Error on line 3 col 20: a"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_float_literal(self):
        input = """
class A {
    var a: float = 123.0;
    var b: float = 0.0;
    var c: float = 1234567890.0;
    var d: float = 1.;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_float_literal_invalid(self):
        input = """
class A {
    var a: float = .12; # missing integer part
}
    """
        expect = "Error on line 3 col 19: ."
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_float_literal_invalid_exponent(self):
        input = """
class A {
    var a: float = 123.0e;
}
    """
        expect = "Error on line 3 col 24: e"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_boolean_literal(self):
        input = """
class A {
    var a: bool = true;
    var b: bool = false;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_string_literal(self):
        input = """
class A {
    var a: string = "Hello World";
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_array_literal(self):
        input = """
class A {
    var a: [5]int = [1,2,3,4,5];
    var b: [5]float = [1.0,2.0,3.0,4.0,5e3];
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_array_literal_invalid(self):
        input = """
class A {
    var a: [5]int = [1;2;3;4;5;6];
}
    """
        expect = "Error on line 3 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 242))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

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

        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_void_type(self):
        input = """
class A {
    func foo(): void {
        var a: string = "Hello" + "World";
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_void_type_not_allowed_variable(self):
        input = """
class A {
    var a: void;
}
    """
        expect = "Error on line 3 col 11: void"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_void_type_not_allowed_parameter(self):
        input = """
class A {
    func foo(a: void): int {}
}
    """
        expect = "Error on line 3 col 16: void"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_void_type_not_allowed_constant(self):
        input = """
class A {
    const a: void = 1;
}
    """
        expect = "Error on line 3 col 13: void"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_array_type_declaration(self):
        input = """
class A {
    var a: [5]int;
    var b: [123]float;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_array_type_declaration_invalid_array_element_type(self):
        input = """
class A {
    var a: [5][5]int;
}
    """
        expect = "Error on line 3 col 11: ["
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_array_type_declaration_invalid_void_element_type(self):
        input = """
class A {
    var a: [5]void;
}
    """
        expect = "Error on line 3 col 11: ["
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_array_type_declaration_invalid_array_size(self):
        input = """
class A {
    var a: [5.0]int;
}
    """
        expect = "Error on line 3 col 11: ["
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_array_type_declaration_invalid_array_size_2(self):
        input = """
class A {
    var a: [0]float;
}
    """
        expect = "Error on line 3 col 11: ["
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_class_type_init(self):
        input = """
class A {
    var a: A = new A();
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_class_type_init_null(self):
        input = """
class A {
    var a: A = null;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_index_operator(self):
        input = """
class A {
    func foo(): int {
        return a[0];
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_index_operator_complex(self):
        input = """
class A {
    func foo(): void {
        a[3+x.foo(2)] := a[b[2]] +3;
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_index_operator_complex2(self):
        input = """
class A {
    func foo(): void {
        x.b[2] := x.m()[3];
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_instance_attribute_access_expression(self):
        input = """
class A {
    func foo(): void {
        x := a.quz().a;
        y := @buzz().a;
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_static_attribute_access(self):
        input = """
class A {
    func foo(): void {
        A.@numOfShape := A.@numOfShape + 1;
        @numOfShape := @numOfShape + 1;
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_variable_declaration_statement_invalid_mismatch_number(self):
        input = """
class A {
    func foo(): void {
        var a, b, c: int = 1, 2;
    }
}
    """
        expect = "Error on line 4 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 268))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_const_declaration_statement_invalid_mismatch_number(self):
        input = """
class A {
    func foo(): void {
        const a, b, c: int = 1, 2;
    }
}
    """
        expect = "Error on line 4 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 270))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_if_statement_invalid_else(self):
        input = """
class A {
    func foo(): void {
        if j > i {j := j - 1;}
        else {j := j + 1;}
        else {j := j + 1;}
    }
}
    """
        expect = "Error on line 6 col 8: else"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_if_statement_invalid_missing_expression(self):
        input = """
class A {
    func foo(): void {
        if {i := 0;} {j := j - 1;} else {j := j + 1;}
    }
}
    """
        expect = "Error on line 4 col 21: {"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_if_statement_invalid_missing_block_statement(self):
        input = """
class A {
    func foo(): void {
        if j > i
        else {j := j + 1;}
    }
}
    """
        expect = "Error on line 5 col 8: else"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_if_statement_invalid_missing_else_block_statement(self):
        input = """
class A {
    func foo(): void {
        if j > i {j := j - 1;}
        else
    }
}
    """
        expect = "Error on line 6 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_for_statement(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; i := i + 1 {
            io.@writeInt(i);
        }

        for @foo(); @bar(); @quz() {
            io.@writeInt(i);
        }
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_for_statement_invalid_missing_statement(self):
        input = """
class A {
    func foo(): void {
        for i < 10; i := i + 1 {
            io.@writeInt(i);
        }
    }
}
    """
        expect = "Error on line 4 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_for_statement_invalid_missing_condition(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i := i + 1 {
            io.@writeInt(i);
        }
    }
}
    """
        expect = "Error on line 4 col 22: :="
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_for_statement_invalid_missing_post_statement(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; {
            io.@writeInt(i);
        }
    }
}
    """
        expect = "Error on line 4 col 28: {"
        self.assertTrue(TestParser.test(input, expect, 280))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_block_statement(self):
        input = """
class A {
    func foo(): void {
        var r, s: tnt;
        r := 2.0;
        var a, b: [5]int;
        s := r * r * self.myPI;
        a[0] := s;
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_block_statement_empty(self):
        input = """
class A {
    func foo(): void {
    }
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_class_invalid_incomplete(self):
        input = """
class A {
    func foo(): void {
    }
    """
        expect = "Error on line 5 col 4: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_attribute_declaration_missing_semicolon(self):
        input = """
class A {
    var a: int
}
    """
        expect = "Error on line 4 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_attribute_declaration_missing_semicolon_2(self):
        input = """
class A {
    var a: int = 1
}
    """
        expect = "Error on line 4 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_method_declaration_missing_block_statement(self):
        input = """
class A {
    func foo(): void
}
    """
        expect = "Error on line 4 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_assignment_statement_missing_semicolon(self):
        input = """
class A {
    func foo(): void {
        self.a := 1
    }
}
    """
        expect = "Error on line 5 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_for_statement_extranous_bracket(self):
        input = """
class A {
    func foo(): void {
        for (i := 0; i < 10; i := i + 1) {
            io.@writeInt(i);
        }
    }
}
    """
        expect = "Error on line 4 col 15: :="
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_break_statement_missing_semicolon(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; i := i + 1 {
            break
        }
    }
}
    """
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_continue_statement_missing_semicolon(self):
        input = """
class A {
    func foo(): void {
        for i := 0; i < 10; i := i + 1 {
            continue
        }
    }
}
    """
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_return_statement_missing_semicolon(self):
        input = """
class A {
    func foo(): void {
        return
    }
}
    """
        expect = "Error on line 5 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_method_invocation_statement_missing_semicolon(self):
        input = """
class A {
    func foo(): void {
        a.foo()
    }
}
    """
        expect = "Error on line 5 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_program_sample_1(self):
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

        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

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
}
    """
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 298))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

