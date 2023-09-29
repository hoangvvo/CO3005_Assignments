grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_dcl+ EOF;

// 2.1 Class declaration
class_dcl: CLASS class_super? ID LP class_body RP;
class_super: ID '<-';
class_body: class_member*;
class_member: attribute | method;

// 2.2 Attribute declaration
attribute: (CONST | VAR) (MEMBER_ID) (CM MEMBER_ID)* COLON type (
		ASSIGN_OP expr (CM expr)*
	)? SEMI;

// 2.3 Method declaration
constructor_method:
	FUNC CONSTRUCTOR LP param_list? RP block_stmt;
method:
	FUNC MEMBER_ID LP param_list? RP COLON (type | VOID) block_stmt;
param_list: param (CM param)*;
param: ID (CM ID)* COLON type;

type: BOOL | INT | FLOAT | STRING | array_type;

// 5 Expressions
expr: expr POW_OP expr1 | expr1;
expr1:
	expr1 (
		EQUAL
		| NOT_EQUAL
		| LESS_THAN
		| GREATER_THAN
		| LESS_EQUAL
		| GREATER_EQUAL
	) expr2
	| expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD_OP | SUB_OP) expr4 | expr4;
expr4:
	expr4 (MUL_OP | DIV_OP | BACKSLASH | MOD_OP) expr5
	| expr5;
expr5: NEGATE expr6 | expr6;
expr6: SUB_OP expr7 | expr7;
expr7: expr7 LS expr8 RS | expr8;
expr8: expr8 DOT ID (LB expr9 (CM expr9)* RB)? | expr9;
expr9: (expr9 DOT)? AT_ID (LB expr10 (CM expr10)* RB)? | expr10;
expr10: NEW ID LB (expr11 (CM expr11)*)? RB | expr11;
expr11: LIT | SELF | ID | LP expr RP;

// 6 Statements 
stmt:
	dcl_stmt
	| assign_stmt
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_invocation_stmt
	| block_stmt;
// 6.1 Variable and Constant Declaration Statement
dcl_stmt: (CONST | VAR) (ID) (CM ID)* COLON type (
		ASSIGN_OP expr (CM expr)*
	)? SEMI;
// 6.2 Assignment Statement TODO: FIXME lhs assign_stmt
assign_stmt: expr DECLARE_ASSIGN_OP expr SEMI;
// 6.3 If Statement
if_stmt: IF block_stmt? expr block_stmt (ELSE block_stmt)?;
// 6.4 For statement
for_stmt: FOR assign_stmt SEMI expr SEMI assign_stmt block_stmt;
// 6.5 Break statement
break_stmt: BREAK SEMI;
// 6.6 Continue statement
continue_stmt: CONTINUE SEMI;
// 6.7 Return statement
return_stmt: RETURN expr? SEMI;
// 6.8 Method Invocation statement
method_invocation_stmt:
	expr DOT ID LB expr (CM expr)* RB SEMI
	| (ID DOT)? AT_ID LB expr (CM expr)* RB SEMI;
// 6.9 Block statement
block_stmt: LP stmt* RP;

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
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';
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
NEGATE: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN_OP: '=';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
DECLARE_ASSIGN_OP: ':=';
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
LIT: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | ARRAY_LIT;
LIT_EXCEPT_ARRAY: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT;

// 3.7.2 Float Literal
FLOAT_LIT: [0-9]+ '.' [0-9]* EXPONENT? | [0-9]+ EXPONENT;
fragment EXPONENT: [eE] [+-]? [0-9]+;
// 3.7.1 Integer literal
INT_LIT: [0-9]+;
// 3.7.3 Boolean literal
BOOL_LIT: TRUE | FALSE;
// 3.7.4 String Literals
STRING_LIT: '"' (ESC | ~["\r\n])* '"';
fragment ESC: '\\' [btnfr"\\];
// 3.7.5 Array Literals
ARRAY_LIT: LS LIT_EXCEPT_ARRAY? (CM LIT_EXCEPT_ARRAY)* RS;

// 4.2 Array type
array_type: LS INT_LIT RS element_type;
element_type: BOOL | INT | FLOAT | STRING;

// 3.3 Identifiers
ID: [A-Za-z_][A-Za-z0-9_]*;
AT_ID: '@' ID;
MEMBER_ID: ID | AT_ID;

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
ERROR_CHAR: . {raise ErrorToken(self.text)};
