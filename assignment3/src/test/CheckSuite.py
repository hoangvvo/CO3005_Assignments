import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):
    def test_redeclared_class(self):
        input = """class a {} class b {} class a {}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_attribute(self):
        input = """class a {var a:int;var c:int;var c:int;}"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_redeclared_class_with_ast(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[])])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_redeclared_attribute_with_ast(self):
        input = Program([ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,404))    
    