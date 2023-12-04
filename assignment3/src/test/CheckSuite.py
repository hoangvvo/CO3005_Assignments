import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_redeclared_class(self):
        input = """class a {} class b {} class a {}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_attribute(self):
        input = """class a {var a:int;var c:int;var c:int;}"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_class_with_ast(self):
        input = Program(
            [ClassDecl(Id("a"), []), ClassDecl(Id("b"), []), ClassDecl(Id("a"), [])]
        )
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_attribute_with_ast(self):
        input = Program(
            [
                ClassDecl(
                    Id("a"),
                    [
                        AttributeDecl(VarDecl(Id("a"), IntType())),
                        AttributeDecl(VarDecl(Id("c"), IntType())),
                        AttributeDecl(VarDecl(Id("c"), IntType())),
                    ],
                )
            ]
        )
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_no_entrypoint(self):
        input = """
        class a {}
        class Program {
            func foo(): void {
                return;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_valid(self):
        input = """
        class Test {
            func foo(): void {
                return;
            }
        }
        class Program {
            func @main(): void {
                return;
            }
            func foo(): void {
                return;
            }
            func bar(foo: int): int {
                return 1;
            }
        }
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_invalid_entrypoint_param(self):
        input = """
        class Program {
            func @main(a: int): void {
                return;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_invalid_entrypoint_rtype(self):
        input = """
        class Program {
            func @main(): int {
                return 1;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared_builtin_class(self):
        input = """
        class io {

        }
        """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_attribute_2(self):
        input = """
        class Program {
            var a: int;
            const a: int = 2;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_attribute_3(self):
        input = """
        class Program {
            const a: int = 1;
            var a: int;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_attribute_4(self):
        input = """
        class A {
            var a: int;
        }
        class Program {
            const a: int = 1;
            const b: int = 2;
            const a: int = 3;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_method(self):
        input = """
        class Program {
            func foo(): void {
                return;
            }
            func foo(): void {
                return;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_method_2(self):
        input = """
        class Bar {
            func bar(): void {
                return;
            }
        }
        class Program {
            var foo: int;
            func bar(): void {
                return;
            }
            func foo(): void {
                return;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_redeclared_method_3(self):
        input = """
        class Bar {
            func bar(): void {
                return;
            }
        }
        class Program {
            var foo: int;
            func foo(): void {
                return;
            }
            func bar(): void {
                return;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_redeclared_method_4(self):
        input = """
        class Bar {
            func bar(): void {
                return;
            }
        }
        class Program {
            var foo: int;
            func bar(): void {
                return;
            }
            func foo(): void {
                return;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_valid_declared_method_1(self):
        input = """
        class Program {
            func foo(): void {
                return;
            }
            func @main(): void {
                return;
            }
        }
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclared_constant(self):
        input = """
        class Program {
            func @main(): void {
                const a: int = 1;
                const a: int = 2;
                return;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redclared_variable(self):
        input = """
        class Program {
            func @main(): void {
                var a: int;
                var a: int;
                return;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_redeclared_parameter(self):
        input = """
        class Program {
            func foo(a: int, a: int): void {
                return;
            }
            func @main(): void {
                return;
            }
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_redeclared_variable_from_param(self):
        input = """
        class Program {
            func foo(a: int): void {
                var a: int;
                return;
            }
            func @main(): void {
                return;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_redclared_const_from_param(self):
        input = """
        class Program {
            func foo(a: int): void {
                const a: int = 1;
                return;
            }
            func @main(): void {
                return;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_redeclared_variable_in_if_block(self):
        input = """
        class Program {
            func @main(): void {
                if 1 + 1 == 2 {
                    var a: int;
                    var a: int;
                }
                return;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_valid_shadowing_variable_if_block(self):
        input = """
        class Program {
            func @main(): void {
                var a: int;
                if 1 + 1 == 2 {
                    var a: int;
                }
                return;
            }
        }
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_redeclared_variable_in_for_block(self):
        input = """
        class Program {
            func @main(): void {
                var i: int;
                for i := 0; i < 10; i := i + 1 {
                    const b: int = 0;
                    var b: int;
                }
                return;
            }
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_valid_shadowing_variable_in_for_block(self):
        input = """
        class Program {
            func @main(): void {
                var i: int;
                const b: int = 0;
                for i := 0; i < 10; i := i + 1 {
                    var b: int;
                }
                return;
            }
        }
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_valid_shadowing_in_param(self):
        input = """
        class Program {
            var a: int;
            func foo(a: int): void {
                return;
            }
            func @main(): void {
                return;
            }
        }
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 427))
