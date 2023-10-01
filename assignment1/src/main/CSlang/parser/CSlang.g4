/* 2152355 */

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
class_member: attribute_decl | method | constructor_method;

// 2.2 Attribute declaration
attribute_decl: attribute_decl_body SEMI;

attribute_decl_body: (CONST | VAR) (
		attribute_decl_inner_with_init
		| attribute_decl_inner_without_init
	);

attribute_decl_inner_without_init: (AT_ID | ID) (CM (AT_ID | ID))* COLON data_type;

attribute_decl_inner_with_init: (AT_ID | ID) attribute_decl_inner_with_init_tail expr;

attribute_decl_inner_with_init_tail:
	CM (AT_ID | ID) attribute_decl_inner_with_init_tail expr CM
	| COLON data_type ASSIGN_OP;

// 2.3 Method declaration
constructor_method:
	FUNC CONSTRUCTOR LB param_list? RB block_stmt;
method:
	FUNC (AT_ID | ID) LB param_list? RB COLON (data_type | VOID) block_stmt;
param_list: param (CM param)*;
param: ID (CM ID)* COLON data_type;

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
array_lit:
	LS (INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT)? (
		CM (INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT)
	)* RS;

// 4 Types and Value
data_type: BOOL | INT | FLOAT | STRING | ARRAY_TYPE | ID;

// 4.2 Array type
fragment ELEMENT_TYPE: BOOL | INT | FLOAT | STRING;
fragment INT_LIT_NON_ZERO: [1-9][0-9]*;
ARRAY_TYPE: LS INT_LIT_NON_ZERO RS ELEMENT_TYPE;

// 5 Expressions
expr:
	LB expr RB
	| <assoc = right> NEW ID LB expr_list? RB
	| (ID DOT)? AT_ID (LB expr_list? RB)?
	| <assoc = left> expr DOT ID (LB expr_list? RB)?
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
expr_list: expr (CM expr)*;

// 6.1 Variable and Constant Declaration Statement
dcl_stmt: attribute_decl;
// 6.2 Assignment Statement TODO: FIXME lhs assign_stmt
assign_stmt_body: expr DECLARE_ASSIGN_OP expr;
assign_stmt: assign_stmt_body SEMI;
// 6.3 If Statement
if_stmt: IF block_stmt? expr block_stmt (ELSE block_stmt)?;
// 6.4 For statement
for_stmt_inner:
	assign_stmt_body
	| method_invocation_stmt_body
	| attribute_decl_body;
for_stmt:
	FOR for_stmt_inner SEMI expr SEMI for_stmt_inner block_stmt;
// 6.5 Break statement
break_stmt: BREAK SEMI;
// 6.6 Continue statement
continue_stmt: CONTINUE SEMI;
// 6.7 Return statement
return_stmt: RETURN expr? SEMI;
// 6.8 Method Invocation statement
method_invocation_stmt_body:
	expr DOT ID LB expr_list? RB
	| (ID DOT)? AT_ID LB expr_list? RB;
method_invocation_stmt: method_invocation_stmt_body SEMI;
// 6.9 Block statement
block_stmt:
	LP (
		dcl_stmt
		| assign_stmt
		| if_stmt
		| for_stmt
		| break_stmt
		| continue_stmt
		| return_stmt
		| method_invocation_stmt
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
