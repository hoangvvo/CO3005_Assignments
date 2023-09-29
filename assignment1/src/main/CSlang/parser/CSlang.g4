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
attribute: (CONST | VAR) (MEMBER_ID) (CM MEMBER_ID)* COLON data_type (
		ASSIGN_OP expr (CM expr)*
	)? SEMI;

// 2.3 Method declaration
constructor_method:
	FUNC CONSTRUCTOR LP param_list? RP block_stmt;
method:
	FUNC MEMBER_ID LP param_list? RP COLON (data_type | VOID) block_stmt;
param_list: param (CM param)*;
param: ID (CM ID)* COLON data_type;

data_type: BOOL | INT | FLOAT | STRING | array_type;

// 5 Expressions
expr: expr_string;
expr_string: expr_string POW_OP expr_rela | expr_rela;
expr_rela:
	expr_rela (
		EQUAL
		| NOT_EQUAL
		| LESS_THAN
		| GREATER_THAN
		| LESS_EQUAL
		| GREATER_EQUAL
	) expr_logic
	| expr_logic;
expr_logic: expr_logic (AND | OR) expr_add | expr_add;
expr_add: expr_add (ADD_OP | SUB_OP) expr_multi | expr_multi;
expr_multi:
	expr_multi (MUL_OP | DIV_OP | BACKSLASH | MOD_OP) expr_logic_not
	| expr_logic_not;
expr_logic_not: NEGATE expr_sign | expr_sign;
expr_sign: SUB_OP expr_index_op | expr_index_op;
expr_index_op:
	expr_index_op LS expr_instance_access RS
	| expr_instance_access;
expr_instance_access:
	expr_instance_access DOT ID (
		LB expr_static_access (CM expr_static_access)* RB
	)?
	| expr_static_access;
expr_static_access: (ID DOT)? AT_ID (
		LB expr_object_creation (CM expr_object_creation)* RB
	)?
	| expr_object_creation;
expr_object_creation:
	NEW ID LB (expr_term (CM expr_term)*)? RB
	| expr_term;
expr_term: LIT | SELF | ID | LP expr RP;

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
dcl_stmt: (CONST | VAR) (ID) (CM ID)* COLON data_type (
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
