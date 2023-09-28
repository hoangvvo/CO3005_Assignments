grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_dcl+ EOF;

// 2.1 Class declaration
class_dcl: CLASS class_super? ID LP class_body? RP;
class_super: ID '<-';
class_body: class_member*;
class_member: attribute | method;
fragment MEMBER_ID: ID | AT_ID;

// 2.2 Attribute declaration
attribute: (CONST | VAR) (MEMBER_ID) (CM MEMBER_ID)* COLON type (
		ASSIGN_OP expr (CM expr)*
	)? SEMI;

// 2.3 Method declaration
constructor_method:
	FUNC CONSTRUCTOR LP param_list? RP block_stmt;
method: FUNC MEMBER_ID LP param_list? RP COLON type block_stmt;
param_list: param (CM param)*;
param: ID (CM ID)* COLON type;

type: BOOL | INT | FLOAT | STRING | VOID | array_type;

// 4.1 Primitive types 4.1.1 Boolean type
bool_op: NEGATE | AND_OP | OR_OP | EQUAL | NOT_EQUAL;
// 4.1.2 Integer type
int_op:
	ADD_OP
	| SUB_OP
	| MUL_OP
	| BACKSLASH
	| MOD_OP
	| EQUAL
	| NOT_EQUAL
	| GREATER_OP
	| GREATER_OR_EQUAL_OP
	| LESS_OP
	| LESS_OR_EQUAL_OP

	// 4.2 Array type An array type declaration is in the form of: ’[’<size>’]’<element_type>. Note
	// that: •<element_type> is the element type of an array. It cannot be array type or, of course,
	// void type. •In an array declaration, it is required that there must be an integer literal
	// between the two square brackets. This number denotes the number (or the length) of that
	// array. The lower bound is always 1. For example, var a: [5]int; indicates a five-element
	// array: a[1], a[2], a[3], a[4], a[5].
	array_type: LS INT_LIT RS;

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
	AND_OP: '&&';
	OR_OP: '||';
	EQUAL: '==';
	ASSIGN_OP: '=';
	NOT_EQUAL: '!=';
	LESS_OP: '<';
	LESS_OR_EQUAL_OP: '<=';
	GREATER_OP: '>';
	GREATER_OR_EQUAL_OP: '>=';
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
	LIT:
		INT_LIT
		| FLOAT_LIT
		| BOOL_LIT
		| STRING_LIT
		| ARRAY_LIT;
	LIT_EXCEPT_ARRAY:
		INT_LIT
		| FLOAT_LIT
		| BOOL_LIT
		| STRING_LIT;

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

	// 3.3 Identifiers
	ID: [A-Za-z_][A-Za-z0-9_]*;
	AT_ID: '@' ID;

	WS: [ \t\r\n]+ -> skip;
	// skip spaces, tabs, newlines

	UNCLOSE_STRING: .;
	ILLEGAL_ESCAPE: .;
	ERROR_CHAR: . {raise ErrorToken(self.text)};
	