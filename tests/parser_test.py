import unittest

from src.lexer import Lexer
from src.parser import Parser

class ParserTest(unittest.TestCase):
    def test_parsing(self):
        json = '{"foo":"bar", "num": 12, "bool": false, "obj": { "inner": "obj" }, "arr": ["first", 12, true]}'

        lex = Lexer(json)
        parser = Parser(lex)

        data = parser.parse()
        
        expectedKeys = ["foo", "num", "bool", "obj", "arr"]

        self.assertEqual(len(data.keys()), len(expectedKeys))

        for key in data.keys():
            self.assertIn(key, expectedKeys)

        self.assertEqual("inner" in data["obj"], True)
        self.assertEqual(True in data["arr"], True)
