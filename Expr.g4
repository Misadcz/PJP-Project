grammar Expr;

/** The start rule; begin parsing here. */
prog: (statement)+;



type : 'int' | 'float' | 'string' | 'bool';
read: 'read' variable (',' variable)* SEMICOLON;
write: 'write' expression (',' expression )* SEMICOLON;
block:  '{' statement* '}';
ifStatement: 'if' '(' expression ')' statement ('else' statement)?;
whileStatement: 'while' '(' expression ')' (statement|block);
forStatement: 'for' '(' assignment SEMICOLON expression SEMICOLON assignment ')' (statement|block);
variable: ID;

statement: read 
        | write 
        | ifStatement 
        | whileStatement 
        | assignment SEMICOLON
        | forStatement
        | block
        |assignmentType SEMICOLON
        ;

assignmentType: type variable ('=' expression)? (',' variable ('=' expression)?)*;

assignment: variable '=' expression     
        | variable '=' assignment       
        ;      
expression:
         expression PLUS expression            
        | expression MINUS expression              
        | expression MULT expression               
        | expression DIV expression                 
        | expression MOD expression                   
        | expression LESSTHAN expression            
        | expression LESSTHANEQUAL expression          
        | expression GREATERTHAN expression          
        | expression GREATERTHANEQUAL expression    
        | expression EQUAL expression                
        | expression NOTEQUAL expression             
        | expression AND expression                    
        | expression OR expression 
        | expression '.' expression
        | expression '?' expression ':' expression
        | '-' expression                
        | NOT expression                              
        | '(' expression ')'                        
        | INT                                          
        | FLOAT                                        
        | STRING                                        
        | BOOL                                          
        | variable                                     
        ;


MOD : '%';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
LESSTHANEQUAL: '<=';
GREATERTHAN: '>';
GREATERTHANEQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';

SEMICOLON: ';';
COMMA: ',';
ID: [a-zA-Z] [a-zA-Z0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ~'"'* '"';
BOOL: 'true' | 'false';
WS: [ \t\n\r]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
