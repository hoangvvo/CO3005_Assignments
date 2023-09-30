import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

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
    def test_keywords(self):
        self.assertTrue(TestLexer.test("break continue if else for true false int float bool string return null class constructor var self new void const func", "break,continue,if,else,for,true,false,int,float,bool,string,return,null,class,constructor,var,self,new,void,const,func,<EOF>", 115))
    def test_operators(self):
        self.assertTrue(TestLexer.test("+-*/\\!&&||===!=<<=>>=:=^new%", "+,-,*,/,\\,!,&&,||,==,=,!=,<,<=,>,>=,:=,^,new,%,<EOF>", 116))
    def test_separators(self):
        self.assertTrue(TestLexer.test("() [ ] .,;:{}", "(,),[,],.,,,;,:,{,},<EOF>", 117))
    def test_integer_literal(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 118))
    def test_float_literal(self):
        self.assertTrue(TestLexer.test("9.0 12e8 1. 0.33E-3 128e+42", "9.0,12e8,1.,0.33E-3,128e+42,<EOF>", 119))
    def test_float_literal_not(self):
        # not literal so parse to different tokens
        self.assertTrue(TestLexer.test(".12 143e 1.2e 1.2e- 1.2e+ 1.2e+e", ".,12,143,e,1.2,e,1.2,e,-,1.2,e,+,1.2,e,+,e,<EOF>", 120))
    def test_boolean_literal(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 121))
    def test_string_literal_escapes(self):
        self.assertTrue(TestLexer.test("""
"This is a string containing tab \\t"
"He asked me: \\"Where is John?\\""
""", "This is a string containing tab \\t,He asked me: \\\"Where is John?\\\",<EOF>", 122))
    def test_string_literal_escape_backslash(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing backslash \\b" """, "This is a string containing backslash \\b,<EOF>", 123))
    def test_string_literal_escape_formfeed(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing formfeed \\f" """, "This is a string containing formfeed \\f,<EOF>", 124))
    def test_string_literal_escape_newline(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing newline \\n New line here" """, "This is a string containing newline \\n New line here,<EOF>", 125))
    def test_string_backslash(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing \\\ backslash" """, "This is a string containing \\\ backslash,<EOF>", 126))
    def test_string_unclosed_string(self):
        self.assertTrue(TestLexer.test(""" "This is an unclosed string """, "Unclosed String: This is an unclosed string ", 127))
