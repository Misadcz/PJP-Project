grammar Expr;

/** The start rule; begin parsing here. */
prog: (statement)+;

ifStatement: 'if' '(' cond ')' (block|statement) ('else' (block | statement))? ;
writeStatement: 'write' variable (',' (variable| cond | ('!' '(' cond ')') ))* ;
readStatement: 'read' ID (',' ID)* ;
forStatement: 'for' '(' assignStatement ';' cond ';' operationStatement ')' (block|statement) ('else' (block | statement))? ;
doWhileStatement: 'do' block 'while' '(' cond ')' ;
whileStatement: 'while' '(' cond ')' block ;

block: '{' statement* '}' 
    | '{' '}' 
    ;

statement: ifStatement
    | variable ';'
    | writeStatement ';'
    | readStatement ';'
    | assignStatement ';'
    | forStatement
    | doWhileStatement
    | whileStatement
    | operationStatement ';'
    ;

cond: variable (comp variable)* 
    | variable
    ;

comp: EQ | NEQ | LT | GT | LE | RE | AND | OR ;

assignStatement: 'int' ID ('=' INT)? (',' ID ('=' INT)?)* 
                | 'float' ID ('=' FLOAT)? (',' ID ('=' FLOAT)?)* 
                | 'string' ID ('=' STRING)? (',' ID ('=' STRING)?)* 
                | 'bool' ID ('=' BOOL)? (',' ID ('=' BOOL)?)* 
                ;

operationStatement: ID (ADD | MUL | DIV | SUB | MOD)? '=' variable 
                | ID '=' variable ((ADD | MUL | DIV | SUB | MOD| '=') variable)+
                | ID (ADD | MUL | DIV | SUB | MOD)? variable
    ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
AND: '&&';
OR: '||';
NOT: '!';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LE: '<=';
RE: '>=';

variable: ID
    | INT
    | FLOAT
    | BOOL
    | STRING
    | '(' variable ')'
    ;

ID: [a-zA-Z]+;
INT: [0-9]+;
STRING: '"' .*? '"' ;
FLOAT: [0-9]+ '.' [0-9]+;
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;