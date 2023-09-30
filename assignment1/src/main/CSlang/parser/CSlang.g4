//
// student ID: 2152355

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
attribute: (CONST | VAR) (
		attribute_inner_with_init
		| attribute_inner_without_init
	) SEMI;

attribute_inner_without_init: (AT_ID | ID) (CM (AT_ID | ID))* COLON data_type;

attribute_inner_with_init: (AT_ID | ID) attribute_inner_with_init_tail expr;

attribute_inner_with_init_tail:
	CM (AT_ID | ID) attribute_inner_with_init_tail expr CM
	| COLON data_type ASSIGN_OP;

// 2.3 Method declaration
constructor_method:
	FUNC CONSTRUCTOR LB param_list? RB block_stmt;
method:
	FUNC (AT_ID | ID) LB param_list? RB COLON (data_type | VOID) block_stmt;
param_list: param (CM param)*;
param: ID (CM ID)* COLON data_type;

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
dcl_stmt: attribute;
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
	expr DOT ID LB expr_list RB SEMI
	| (ID DOT)? AT_ID LB expr_list RB SEMI;
// 6.9 Block statement
block_stmt: LP stmt* RP;

// 5 Expressions
expr:
	LB expr RB
	| <assoc = right> NEW ID LB (expr_list)? RB
	| (ID DOT)? AT_ID (LB expr_list RB)?
	| <assoc = left> expr DOT ID (LB expr_list RB)?
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
	| LIT
	| SELF
	| ID;
expr_list: expr (CM expr)*;

data_type: BOOL | INT | FLOAT | STRING | array_type;

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
LIT:
	INT_LIT
	| FLOAT_LIT
	| BOOL_LIT
	| STRING_LIT {self.text = self.text[1:-1]}
	| ARRAY_LIT;
LIT_EXCEPT_ARRAY: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT;

// 3.7.2 Float Literal
FLOAT_LIT: [0-9]+ '.' [0-9]* EXPONENT? | [0-9]+ EXPONENT;
fragment EXPONENT: [eE] [+-]? [0-9]+;
// 3.7.1 Integer literal
INT_LIT: [0-9]+;
// 3.7.3 Boolean literal
BOOL_LIT: TRUE | FALSE;
// 3.7.4 String Literals
fragment CHAR_LIT: ~["\\\r\n'] | ESC | '\'"';
fragment ESC: '\\' [bfrnt"\\];
STRING_LIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};

// 3.7.5 Array Literals
ARRAY_LIT: LS LIT_EXCEPT_ARRAY? (CM LIT_EXCEPT_ARRAY)* RS;

// 4.2 Array type
array_type: LS INT_LIT RS element_type;
element_type: BOOL | INT | FLOAT | STRING;

// 3.3 Identifiers
ID: [A-Za-z_][A-Za-z0-9_]*;
AT_ID: '@' [A-Za-z0-9_]+;

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

UNCLOSE_STRING:
	'"' CHAR_LIT* {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE:
	'"' CHAR_LIT* ('\\' ~([bfrnt\\] | '\'')) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};
