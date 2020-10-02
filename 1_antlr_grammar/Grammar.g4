/* nome da gramática -- deve ser o mesmo nome do arquivo .g4 e começar com letra maiúscula*/
grammar Grammar;

/* parser */
/* regra raiz */
file
	: (variable_definition SEMICOLON | function_definition)*
	;

/* regra que descreve a definição de uma função. */
function_definition
	: type identifier arguments body;

/* regra que define o formato dos argumentos na declaração de uma função. */
arguments
	: '(' (type identifier ','?)* ')';

/* regra que descreve um statement dentro de chaves (‘{‘ e ‘}’). */
body 
	: '{' statement* '}';

/* regra que conterá diferentes tipos de statements. */
statement
    : if_statement
	| for_loop
	| expression SEMICOLON
	| variable_definition SEMICOLON
	| variable_assignment SEMICOLON
	| RETURN expression SEMICOLON
	;

/*  regra que define o formato de um ‘if’. */
if_statement
	: 'if' expression body else_statement*
    | 'if' expression statement
	;

/* regra que define o formato de um ‘else’. */
else_statement
	: 'else' body
    | 'else' if_statement
	;

/*  regra que define o formato do ‘for’. */
for_loop
	: 'for' '(' for_initializer SEMICOLON for_condition SEMICOLON for_step ')' body
	;

/* regra que define o formato do primeiro parâmetro do ‘for’, o inicializador. */
for_initializer
	: variable_assignment 
    | variable_definition
	;

/* regra que define o formato da condição do‘for’. */
for_condition
	: expression
	;

/* regra que define o formato do step do ‘for’. */
for_step
	: variable_assignment
	;

/* regra que define o formato de uma definição de variável. */
variable_definition
	: type (identifier '=' expression ','?)+
    | type (array '=' array_literal? ','?)+
    ;

/* regra que define o formato da atribuição de um valor a uma variável. */
variable_assignment
	: identifier '=' expression
	| identifier ('+='|'-=') expression
	| identifier ('/='|'*=') expression
	| identifier ('++'|'--')
	| ('++'|'--') identifier 
	;

/* regra que define os diferentes tipos de expressões presentes na linguagem (aritmética, chamada de função, etc). */
expression
	: string
	| integer
	| floating
	| function_call
    | array
	| identifier
    | expression ('<'|'>'|'<='|'>=') expression
    | expression ('!='|'==') expression
	| expression ('/'|'*') expression
	| expression ('+'|'-') expression
	| ('-') expression
	| '(' expression ')'
	;
/* regra que define o formato do array na linguagem. */
array
    : identifier '[' expression ']' 
    ;

/* regra que define um array literal. Ex.: {1, 2, 3}. */
array_literal
    : '{' (expression ','?)* '}' 
    ;

/*  regra que define o formato da chamada de uma função. */
function_call: identifier '(' (expression ','?)* ')';

/*  regra que define os tipos presentes na linguagem. */
type: TYPE;
identifier : IDENTIFIER;
string : STRING;
integer : INTEGER_NUMBER;
floating : FLOATING_NUMBER;

/* lexer */
WHITESPACE : [ \t]+ -> skip;
NEWLINE : ('\r' '\n'? | '\n') -> skip;
BLOCKCOMMENT : '/*' .*? '*/' -> skip;
LINECOMMENT : '//' ~[\r\n]* -> skip;
PRE_PROCESSING_DIRECTIVES : '#' ~[\r\n]* -> skip;
SEMICOLON : (';');
RETURN : ('return');
TYPE : ('int'|'float');
STRING: '"' .*? '"';
INTEGER_NUMBER : [0-9]+;
FLOATING_NUMBER : [0-9]+'.'?[0-9]*;
IDENTIFIER : ([a-zA-Z_]+[0-9]*);

/*
MANUAL

caracteres especiais para expressões regulares {
	'xyz'   :  os caracteres rodeados por ' ' são interpretados literalmente 
	\x		:  altera a interpretação do caracter x, se ele tiver outra (\t: tab, \(: o caracter que abre parênteses)
	a(bc)d  :  destaca a subexpressão bc
	x | y   :  aceita a subexpressão x ou y
	[x\yz]	:  equivalente a ('x'|\y|'z'), tal que x, \y e z são caracteres
	[x]		:  equivalente a 'x'
	x*		:  aceita 0 ou mais x's
	x+		:  aceita 1 ou mais x's
	x?		:  aceita 0 ou 1 x
	.       :  aceita qualquer caracter
	.*      :  aceita 0 ou mais caracteres diferentes de \n (guloso)
	.*?     :  aceita 0 ou mais caracteres diferentes de \n (não-guloso)

	regex -> skip : qualquer instância da expressão regular regex não é passada para o parser, sendo assim ignorada (usado em comentários, espaços em branco, ou (no caso deste exercício) diretivas de preprocessamento)


	no ANTLR alguns desses caracteres especiais podem ser utilizados nas regras da gramática também
	ex.:
		expr ('+'|'-') expr
	estabelece que os dois sinais têm a mesma precedência
		'(' (expr (',' expr)*)? ')'
	indica que dentro destes parênteses pode haver zero ou mais expressões separadas por vírgulas
}

regras da gramática {
	nome_da_regra
		: uma seqüência de regras que satisfazem esta
		| outra
		| e mais outra
		;

	NOME_DA_EXPRESSÃO_REGULAR : a_expressão_regular ;

	dentro de uma regra a primeira opção tem maior precedência (útil em expressões matemáticas)
}
*/
