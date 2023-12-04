/* 2152355 */

grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classdecl+ EOF;

// 2.1 Class declaration
classdecl: CLASS classsuper? ID LP memdecl* RP;
classsuper: ID '<-';
memdecl: attributedecl | methoddecl | constructormethod;

// 2.2 Attribute declaration
attributedecl: attributedecl_body SEMI;

attributedecl_body:
	VAR (
		attributedecl_inner_with_init
		| attributedecl_inner_without_init
	)
	| CONST attributedecl_inner_with_init;

attributedecl_inner_without_init: (AT_ID | ID) (CM (AT_ID | ID))* COLON cslangtype;

attributedecl_inner_with_init: (AT_ID | ID) attributedecl_inner_with_init_tail expr;

attributedecl_inner_with_init_tail:
	CM (AT_ID | ID) attributedecl_inner_with_init_tail expr CM
	| COLON cslangtype ASSIGN_OP;

// 2.3 Method declaration
constructormethod: FUNC CONSTRUCTOR LB paramlist? RB blockstmt;
methoddecl:
	FUNC (AT_ID | ID) LB paramlist? RB COLON (cslangtype | VOID) blockstmt;
paramlist: param (CM param)*;
param: ID (CM ID)* COLON cslangtype;

// 3.2 Program comment
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// 3.4 Keywords
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
INTTYPE: 'int';
FLOATTYPE: 'float';
BOOLTYPE: 'bool';
STRINGTYPE: 'string';
RETURN: 'return';
NULL: 'null';
CLASS: 'class';
CONSTRUCTOR: 'constructor';
VAR: 'var';
SELF: 'self';
NEW: 'new';
VOID: 'void';
CONST: 'const';
FUNC: 'func';

// 3.5 Operators
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
BACKSLASH: '\\';
NOT_EQUAL: '!=';
NEGATE: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
DECLARE_ASSIGN_OP: ':=';
ASSIGN_OP: '=';
LESS_EQUAL: '<=';
LESS_THAN: '<';
GREATER_EQUAL: '>=';
GREATER_THAN: '>';
POW_OP: '^';
// NEW: 'new';
MOD_OP: '%';

// 3.6 Separators
LB: '(';
RB: ')';
LS: '[';
RS: ']';
DOT: '.';
CM: ',';
LP: '{';
RP: '}';
SEMI: ';';
COLON: ':';

// 3.7 Literals

// 3.7.2 Float Literal
FLOAT_LIT: [0-9]+ '.' [0-9]* EXPONENT? | [0-9]+ EXPONENT;
fragment EXPONENT: [eE] [+-]? [0-9]+;
// 3.7.1 Integer literal
INT_LIT: [0-9]+;
// 3.7.3 Boolean literal

// 3.7.4 String Literals
fragment CHAR_LIT: ~["\\\r\n'] | ESC | '\'"';
fragment ESC: '\\' [bfrnt"\\];
STRING_LIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};

// 3.7.5 Array Literals
// 
// not a literal: https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=12968#p39025
array_lit: LS lit? (CM lit)* RS;

lit: INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT;

// 4 Types and Value
cslangtype:
	BOOLTYPE
	| INTTYPE
	| FLOATTYPE
	| STRINGTYPE
	| arraytype
	| ID;

// 4.2 Array type
// 
// ARRAYSIZE: [1-9][0-9]*;
elementtype: BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE | ID;
arraytype: LS INT_LIT RS elementtype;

// 5 Expressions
expr:
	LB expr RB
	| <assoc = right> NEW ID LB exprlist? RB
	| (ID DOT)? AT_ID (LB exprlist? RB)?
	| <assoc = left> expr DOT ID (LB exprlist? RB)?
	| expr LS expr RS
	| <assoc = right> SUB_OP expr
	| <assoc = right> NEGATE expr
	| <assoc = left> expr (MUL_OP | DIV_OP | BACKSLASH | MOD_OP) expr
	| <assoc = left> expr (ADD_OP | SUB_OP) expr
	| <assoc = left> expr (AND | OR) expr
	| expr (
		EQUAL
		| NOT_EQUAL
		| LESS_THAN
		| GREATER_THAN
		| LESS_EQUAL
		| GREATER_EQUAL
	) expr
	| expr POW_OP expr
	| (
		INT_LIT
		| FLOAT_LIT
		| TRUE
		| FALSE
		| STRING_LIT
		| array_lit
		| NULL
	)
	| SELF
	| ID;
exprlist: expr (CM expr)*;

// 6.1 Variable and Constant Declaration Statement
dclstmt: attributedecl;
// 6.2 Assignment Statement TODO: FIXME lhs assignstmt
assignstmt_body: expr DECLARE_ASSIGN_OP expr;
assignstmt: assignstmt_body SEMI;
// 6.3 If Statement
ifstmt: IF blockstmt? expr blockstmt (ELSE blockstmt)?;
// 6.4 For statement
forstmt_inner:
	assignstmt_body
	| methodinvocationstmt_body
	| attributedecl_body;
forstmt:
	FOR forstmt_inner SEMI expr SEMI forstmt_inner blockstmt;
// 6.5 Break statement
breakstmt: BREAK SEMI;
// 6.6 Continue statement
continuestmt: CONTINUE SEMI;
// 6.7 Return statement
returnstmt: RETURN expr? SEMI;
// 6.8 Method Invocation statement
methodinvocationstmt_body:
	expr DOT ID LB exprlist? RB
	| (ID DOT)? AT_ID LB exprlist? RB;
methodinvocationstmt: methodinvocationstmt_body SEMI;
// 6.9 Block statement
blockstmt:
	LP (
		dclstmt
		| assignstmt
		| ifstmt
		| forstmt
		| breakstmt
		| continuestmt
		| returnstmt
		| methodinvocationstmt
	)* RP;

// 3.3 Identifiers
ID: [A-Za-z_][A-Za-z0-9_]*;
AT_ID: '@' [A-Za-z0-9_]+;

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

UNCLOSE_STRING:
	'"' CHAR_LIT* {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: (
		'"' ('\\' [bfrnt\\'] | ~[\n\r\\"])* ('\\' (~[bfrnt'\\]))
	) {raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};