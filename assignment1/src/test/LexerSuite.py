import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 100))
    def test_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_underscore_identifier(self):
        self.assertTrue(TestLexer.test(""" _abc """, "_abc,<EOF>", 102))
    def test_class_definition(self):
        self.assertTrue(TestLexer.test(""" class Foo { } """, "class,Foo,{,},<EOF>", 103))
    def test_class_definition_with_super(self):
        self.assertTrue(TestLexer.test(""" class Shape <- Rectangle { } """, "class,Shape,<-,Rectangle,{,},<EOF>", 104))
    def test_function_definition(self):
        self.assertTrue(TestLexer.test(""" func someId(a, b, c: int): void { } """, "func,someId,(,a,,,b,,,c,:,int,),:,void,{,},<EOF>", 105))
    def test_variable_declaration(self):
        self.assertTrue(TestLexer.test(""" var a, b, c: int = 1, 2, 3; """, "var,a,,,b,,,c,:,int,=,1,,,2,,,3,;,<EOF>", 106))
    def test_line_comment(self):
        self.assertTrue(TestLexer.test("""a: = 5 // This is a comment """, "a,:,=,5,<EOF>", 107))
    def test_block_comment(self):
        self.assertTrue(TestLexer.test("""a: = 5 /* This is a \n block comment */ """, "a,:,=,5,<EOF>", 108))
    def test_line_comment_inside_block_comment(self):
        self.assertTrue(TestLexer.test("""a: = 5 /* This is a // block comment */ """, "a,:,=,5,<EOF>", 109))
    def test_block_comment_inside_line_comment(self):
        self.assertTrue(TestLexer.test("""a: = 5 // This is a /* block comment */ """, "a,:,=,5,<EOF>", 110))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("a12_3b", "a12_3b,<EOF>", 111))
    def test_non_id_begins_nonletter(self):
        self.assertTrue(TestLexer.test("1a1", "1,a1,<EOF>", 112))
    def test_at_id(self):
        self.assertTrue(TestLexer.test("@ab2c", "@ab2c,<EOF>", 113))
    def test_at_id_begins_nonletter(self):
        self.assertTrue(TestLexer.test("@123abc", "@123abc,<EOF>", 114))
    def test_break_keyword(self):
        self.assertTrue(TestLexer.test("break", "break,<EOF>", 115))
        
    def test_continue_keyword(self):
        self.assertTrue(TestLexer.test("continue", "continue,<EOF>", 116))
        
    def test_if_keyword(self):
        self.assertTrue(TestLexer.test("if", "if,<EOF>", 117))
        
    def test_else_keyword(self):
        self.assertTrue(TestLexer.test("else", "else,<EOF>", 118))
        
    def test_for_keyword(self):
        self.assertTrue(TestLexer.test("for", "for,<EOF>", 119))
        
    def test_true_keyword(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 120))
        
    def test_false_keyword(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 121))
        
    def test_int_keyword(self):
        self.assertTrue(TestLexer.test("int", "int,<EOF>", 122))
        
    def test_float_keyword(self):
        self.assertTrue(TestLexer.test("float", "float,<EOF>", 123))
        
    def test_bool_keyword(self):
        self.assertTrue(TestLexer.test("bool", "bool,<EOF>", 124))
        
    def test_string_keyword(self):
        self.assertTrue(TestLexer.test("string", "string,<EOF>", 125))
        
    def test_return_keyword(self):
        self.assertTrue(TestLexer.test("return", "return,<EOF>", 126))
        
    def test_null_keyword(self):
        self.assertTrue(TestLexer.test("null", "null,<EOF>", 127))
        
    def test_class_keyword(self):
        self.assertTrue(TestLexer.test("class", "class,<EOF>", 128))
        
    def test_constructor_keyword(self):
        self.assertTrue(TestLexer.test("constructor", "constructor,<EOF>", 129))
        
    def test_var_keyword(self):
        self.assertTrue(TestLexer.test("var", "var,<EOF>", 130))
        
    def test_self_keyword(self):
        self.assertTrue(TestLexer.test("self", "self,<EOF>", 131))
        
    def test_new_keyword(self):
        self.assertTrue(TestLexer.test("new", "new,<EOF>", 132))
        
    def test_void_keyword(self):
        self.assertTrue(TestLexer.test("void", "void,<EOF>", 133))
        
    def test_const_keyword(self):
        self.assertTrue(TestLexer.test("const", "const,<EOF>", 134))
        
    def test_func_keyword(self):
        self.assertTrue(TestLexer.test("func", "func,<EOF>", 135))
    def test_operators(self):
        self.assertTrue(TestLexer.test("+-*/\\!&&||===!=<<=>>=:=^new%", "+,-,*,/,\\,!,&&,||,==,=,!=,<,<=,>,>=,:=,^,new,%,<EOF>", 136))
    def test_separators(self):
        self.assertTrue(TestLexer.test("() [ ] .,;:{}", "(,),[,],.,,,;,:,{,},<EOF>", 137))
    def test_integer_literal(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 138))
    def test_float_literal_1(self):
        self.assertTrue(TestLexer.test("9.0 10.0 1.0 0.33334 128.0", "9.0,10.0,1.0,0.33334,128.0,<EOF>", 139))
    def test_float_literal_2(self):
        self.assertTrue(TestLexer.test("12E8 4e5 1999E9991 128e+42", "12E8,4e5,1999E9991,128e+42,<EOF>", 140))
    def test_float_literal_3(self):
        self.assertTrue(TestLexer.test("0.33e5 0.33e-5 0.33E+5 0.33E-5", "0.33e5,0.33e-5,0.33E+5,0.33E-5,<EOF>", 141))
    def test_float_literal_not(self):
        # not literal so parse to different tokens
        self.assertTrue(TestLexer.test(".12 143e 1.2e 1.2e- 1.2e+ 1.2e+e", ".,12,143,e,1.2,e,1.2,e,-,1.2,e,+,1.2,e,+,e,<EOF>", 142))
    def test_boolean_literal(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 143))
    def test_string_literal_escapes_tab(self):
        self.assertTrue(TestLexer.test("""
"This is a string containing tab \\t"
""", "This is a string containing tab \\t,<EOF>", 144))
    def test_string_literal_escape_backslash(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing backslash \\b" """, "This is a string containing backslash \\b,<EOF>", 145))
    def test_string_literal_escape_formfeed(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing formfeed \\f" """, "This is a string containing formfeed \\f,<EOF>", 146))
    def test_string_literal_escape_newline(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing newline \\n New line here" """, "This is a string containing newline \\n New line here,<EOF>", 147))
    def test_string_backslash(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing \\\ backslash" """, "This is a string containing \\\ backslash,<EOF>", 148))
    def test_string_unclosed_string(self):
        self.assertTrue(TestLexer.test(""" "This is an unclosed string""", "Unclosed String: This is an unclosed string", 149))
    def test_string_ill_escape(self):
        self.assertTrue(TestLexer.test(""" "This is an illegal escape string \\a""", "Illegal Escape In String: This is an illegal escape string \\a", 150))
    def test_array_literal(self):
        self.assertTrue(TestLexer.test("[1, 2, 3] [2.3, 4.2, 102e3]", "[,1,,,2,,,3,],[,2.3,,,4.2,,,102e3,],<EOF>", 151))
    def test_array_literal_empty(self):
        self.assertTrue(TestLexer.test("[]", "[,],<EOF>", 152))
    def test_primitive_boolean_type(self):
        self.assertTrue(TestLexer.test("boolA && boolB || !boolC == true && boolE != false",
        "boolA,&&,boolB,||,!,boolC,==,true,&&,boolE,!=,false,<EOF>",
        153))
    def test_primitive_int_type(self):
        self.assertTrue(TestLexer.test("intA + 0 - intC * 128 / intE % intF",
        "intA,+,0,-,intC,*,128,/,intE,%,intF,<EOF>",
        154))
    def test_primitive_float_type(self):
        self.assertTrue(TestLexer.test("floatA + 0.0 - floatC * 128.0 / floatE % 12.08e-5",
        "floatA,+,0.0,-,floatC,*,128.0,/,floatE,%,12.08e-5,<EOF>",
        155))
    def test_primitive_string_type(self):
        self.assertTrue(TestLexer.test(""" "stringA" ^ "stringB" """,
        "stringA,^,stringB,<EOF>",
        156))
    def test_primitive_void(self):
        self.assertTrue(TestLexer.test("func foo(): void", "func,foo,(,),:,void,<EOF>", 157))
    def test_primitive_type_array(self):
        self.assertTrue(TestLexer.test("var a: [5]int; a[1] a[2] a[4+5]", "var,a,:,[5]int,;,a,[,1,],a,[,2,],a,[,4,+,5,],<EOF>", 158))
    def test_primitive_class_type(self):
        self.assertTrue(TestLexer.test("var a: X = new X();", "var,a,:,X,=,new,X,(,),;,<EOF>", 159))
    def test_primitive_class_type_with_param(self):
        self.assertTrue(TestLexer.test("var a: X = new X(1, 2, 3);", "var,a,:,X,=,new,X,(,1,,,2,,,3,),;,<EOF>", 160))
    def test_primitive_class_type_null(self):
        self.assertTrue(TestLexer.test("var a: X = null;", "var,a,:,X,=,null,;,<EOF>", 161))
    def test_arithmetic_operators(self):
        self.assertTrue(TestLexer.test("1.0e8 + b - c * 123 / e % f", "1.0e8,+,b,-,c,*,123,/,e,%,f,<EOF>", 162))
    def test_boolean_opeators(self):
        self.assertTrue(TestLexer.test("a && b || !c == true && e != false", "a,&&,b,||,!,c,==,true,&&,e,!=,false,<EOF>", 163))
    def test_string_operators(self):
        self.assertTrue(TestLexer.test(""" "stringA" ^ "stringB" """, "stringA,^,stringB,<EOF>", 164))
    def test_ralational_operators(self):
        self.assertTrue(TestLexer.test("a < b <= c > d >= e == f != g", "a,<,b,<=,c,>,d,>=,e,==,f,!=,g,<EOF>", 165))
    def test_index_operator(self):
        self.assertTrue(TestLexer.test("a[1] b[2] c[3]", "a,[,1,],b,[,2,],c,[,3,],<EOF>", 166))
    def test_index_operator_complex(self):
        self.assertTrue(TestLexer.test("a[3+x.foo(2)] := a[b[2]] +3;", "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>", 167))
    def test_index_operator_complex_2(self):
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3];", "x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,<EOF>", 168))
    def test_instance_attribute_access(self):
        self.assertTrue(TestLexer.test("x.foo y.bar z.baz", "x,.,foo,y,.,bar,z,.,baz,<EOF>", 169))
    def test_instance_attribute_access_complex(self):
        self.assertTrue(TestLexer.test("x.foo.bar.quz", "x,.,foo,.,bar,.,quz,<EOF>", 170))
    def test_static_attribute_access(self):
        self.assertTrue(TestLexer.test("SomeClass.@foo SomeOtherClass.@123", "SomeClass,.,@foo,SomeOtherClass,.,@123,<EOF>", 171))
    def test_static_attribute_access_omit_class(self):
        self.assertTrue(TestLexer.test("@foo @123", "@foo,@123,<EOF>", 172))
    def test_instance_method_invocation(self):
        self.assertTrue(TestLexer.test("x.foo() y.bar(a, b) z.baz(1, 5.2e8)", "x,.,foo,(,),y,.,bar,(,a,,,b,),z,.,baz,(,1,,,5.2e8,),<EOF>", 173))
    def test_instance_method_invocation_complex(self):
        self.assertTrue(TestLexer.test("x.foo().bar().quz()", "x,.,foo,(,),.,bar,(,),.,quz,(,),<EOF>", 174))
    def test_static_method_invocation(self):
        self.assertTrue(TestLexer.test("SomeClass.@foo() SomeOtherClass.@123()", "SomeClass,.,@foo,(,),SomeOtherClass,.,@123,(,),<EOF>", 175))
    def test_static_method_invocation_omit_class(self):
        self.assertTrue(TestLexer.test("@foo() @123()", "@foo,(,),@123,(,),<EOF>", 176))
    def test_object_creation(self):
        self.assertTrue(TestLexer.test("new SomeClass() new SomeOtherClass(1, 2, 3)", "new,SomeClass,(,),new,SomeOtherClass,(,1,,,2,,,3,),<EOF>", 177))
    def test_self(self):
        self.assertTrue(TestLexer.test("self self.foo self.bar()", "self,self,.,foo,self,.,bar,(,),<EOF>", 178))
    def test_statement_variable_declaration(self):
        self.assertTrue(TestLexer.test("var a, b, c: int = foo(x, y, z), X.foo, @bar(n);", "var,a,,,b,,,c,:,int,=,foo,(,x,,,y,,,z,),,,X,.,foo,,,@bar,(,n,),;,<EOF>", 179))
    def test_statement_variable_declaration_no_init(self):
        self.assertTrue(TestLexer.test("var a, b, c: int;", "var,a,,,b,,,c,:,int,;,<EOF>", 180))
    def test_statement_const_declaration(self):
        self.assertTrue(TestLexer.test("const a, b, c: int = foo(x, y, z), X.foo, @bar(n);", "const,a,,,b,,,c,:,int,=,foo,(,x,,,y,,,z,),,,X,.,foo,,,@bar,(,n,),;,<EOF>", 181))
    def test_statement_const_declaration_no_init(self):
        self.assertTrue(TestLexer.test("const a, b, c: int;", "const,a,,,b,,,c,:,int,;,<EOF>", 182))
    def test_assignment_statement(self):
        self.assertTrue(TestLexer.test("a := 123; b := 1.2e8; c := \"string\"; d := true; e := false;", "a,:=,123,;,b,:=,1.2e8,;,c,:=,string,;,d,:=,true,;,e,:=,false,;,<EOF>", 183))
    def test_assignment_statement_complex(self):
        self.assertTrue(TestLexer.test("a := foo(x, y, z); b := X.foo; c := @bar(n);", "a,:=,foo,(,x,,,y,,,z,),;,b,:=,X,.,foo,;,c,:=,@bar,(,n,),;,<EOF>", 184))
    def test_assignmenet_lhs(self):
        self.assertTrue(TestLexer.test("a[1] := 2; b.foo := 3; c.@bar := 4;", "a,[,1,],:=,2,;,b,.,foo,:=,3,;,c,.,@bar,:=,4,;,<EOF>", 185))
    def test_if_statement(self):
        self.assertTrue(TestLexer.test("if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}", "if,{,i,:=,0,;,},j,>,i,{,j,:=,j,-,1,;,},else,{,j,:=,j,+,1,;,},<EOF>", 186))
    def test_if_statement_no_else(self):
        self.assertTrue(TestLexer.test("if {i := 0;} j > i {j := j - 1;}", "if,{,i,:=,0,;,},j,>,i,{,j,:=,j,-,1,;,},<EOF>", 187))
    def test_for_statement(self):
        self.assertTrue(TestLexer.test("""
for i := 0; i < 10; i := i + 1 {
io.@writeInt(i);
}
""", "for,i,:=,0,;,i,<,10,;,i,:=,i,+,1,{,io,.,@writeInt,(,i,),;,},<EOF>", 188))
    def test_break_statement(self):
        self.assertTrue(TestLexer.test("break;", "break,;,<EOF>", 189))
    def test_continue_statement(self):
        self.assertTrue(TestLexer.test("continue;", "continue,;,<EOF>", 190))
    def test_return_statement(self):
        self.assertTrue(TestLexer.test("return;", "return,;,<EOF>", 191))
    def test_return_statement_with_expression(self):
        self.assertTrue(TestLexer.test("return 1 + 2;", "return,1,+,2,;,<EOF>", 192))
    def test_method_invocation_statement(self):
        self.assertTrue(TestLexer.test("Shape.@getNumOfShape();" , "Shape,.,@getNumOfShape,(,),;,<EOF>", 193))
    def test_block_statement(self):
        self.assertTrue(TestLexer.test("""
{
var r, s: tnt;
r := 2.0;
var a, b: [5]int;
s := r * r * self.myPI;
a[0] := s;
}""", "{,var,r,,,s,:,tnt,;,r,:=,2.0,;,var,a,,,b,:,[5]int,;,s,:=,r,*,r,*,self,.,myPI,;,a,[,0,],:=,s,;,},<EOF>", 194))
    def test_block_statement_empty(self):
        self.assertTrue(TestLexer.test("{       }", "{,},<EOF>", 195))
    def test_block_statement_nested(self):
        self.assertTrue(TestLexer.test("""
class Shape {
    func foo() {

    }
}""", "class,Shape,{,func,foo,(,),{,},},<EOF>", 196))
    def test_io_calls(self):
        self.assertTrue(TestLexer.test("""
io.@readInt();
io.@writeInt(123);
io.@readFloat();
io.@writeFloat(123.0);
io.@readBool();
io.@writeBool(true);
io.@readStr();
io.@writeStr("Some string");
""", "io,.,@readInt,(,),;,io,.,@writeInt,(,123,),;,io,.,@readFloat,(,),;,io,.,@writeFloat,(,123.0,),;,io,.,@readBool,(,),;,io,.,@writeBool,(,true,),;,io,.,@readStr,(,),;,io,.,@writeStr,(,Some string,),;,<EOF>", 197))
    def test_string_literal_escape_double_quote(self):
        self.assertTrue(TestLexer.test("""
"He asked me: \\"Where is John?\\""
""", "He asked me: \\\"Where is John?\\\",<EOF>", 198))
    def test_empty_2(self):
        self.assertTrue(TestLexer.test(" \t \n \r", "<EOF>", 199))