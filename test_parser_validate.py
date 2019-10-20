import unittest
from sys import maxsize
from parser import Parser
from random import randint
from ll1_table import table, terminals
# from string import printable
# from invalid_symbol_error import InvalidSymbolError

class TestParserValidate(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestParserValidate, self).__init__(*args, **kwargs)
        self.parser = Parser(table, terminals)

    def test_add_one(self):
        self.assertTrue(self.parser.validate("(x+1);"))

    def test_empty_string(self):
        self.assertTrue(self.parser.validate(""))

    def test_let_while(self):
        self.assertTrue(self.parser.validate("letx=(y-20);while1doy;;"))

    def test_let_while_with_spaces(self):
        self.assertTrue(self.parser.validate("let x=(y-20);while 1 do y;;"))

    def test_multi_line_let_while(self):
        string = '''let x=(y-20);wh
                        il
                    e 1 do y;;'''
        self.assertTrue(self.parser.validate(string))

    def test_let_with_spaces(self):
        self.assertTrue(self.parser.validate("let x = y;"))

    def test_number(self):
        self.assertTrue(self.parser.validate("158;"))

    def test_sequential_variables_with_newline(self):
        string = '''x;
                    y;
                    z;
                '''
        self.assertTrue(self.parser.validate(string))

    def test_sequential_variables(self):
        self.assertTrue(self.parser.validate("x;y;z;"))

    def test_additional_parentheses(self):
        self.assertFalse(self.parser.validate("(1);"))

    def test_hanging_parentheses(self):
        self.assertFalse(self.parser.validate("(x+1));"))
        self.assertFalse(self.parser.validate("((x+1);"))

    def test_unterminated_else(self):
        self.assertFalse(self.parser.validate("while 1 do x; else y;"))

    def test_unrecognised_variable(self):
        self.assertFalse(self.parser.validate("xx;"))

    def test_zero(self):
        self.assertFalse(self.parser.validate("0;"))

    def test_integer_with_semi_colon(self):
        self.assertTrue(self.parser.validate(str(randint(1, maxsize))+ ";"))

    def test_integer_without_semi_colon(self):
        self.assertFalse(self.parser.validate(str(randint(1, maxsize))))


if __name__ == '__main__':
    unittest.main()

