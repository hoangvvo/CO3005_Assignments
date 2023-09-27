grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: ID EOF;

ID: [a-z]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

// For lexical errors, please return the following tokens together with specific lexemes: –
// ERROR_TOKEN with <unrecognized char> lexeme: when the lexer detects an unrecognized character. –
// UNCLOSE_STRING with <unclosed string> lexeme: when the lexer detects an unterminated string. The
// <unclosed string> lexeme does not include the opening quote. – ILLEGAL_ESCAPE with <wrong string>
// lexeme: when the lexer detects an illegal escape in string. The wrong string is from the
// beginning of the string (without the opening quote) to the illegal escape.

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;