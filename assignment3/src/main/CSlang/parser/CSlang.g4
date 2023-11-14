grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: classdecl+ EOF ;

classdecl: 'class' ID '{' memdecl* '}' ;

memdecl: 'var' ID ':' cslangtype ';';

cslangtype : INTTYPE | VOIDTYPE;

INTTYPE: 'int';

VOIDTYPE: 'void';

ID: [a-z]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;