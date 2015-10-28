/* Dzu Pham
 * lexer.l
 *
 */

%{
/*This is vitally important*/
/* Definitions of constants, vars, function prototypes, and #includes go here*/

#define T_IDENT    1
#define T_INTCONST 2
#define T_HEXCONST 3
#define T_DECCONST 4
#define T_COMMENT  5
#define T_SCICONST 6
#define T_OPERATOR 7
#define T_KEYWORD  8
#define T_STRCONST 9
#define T_INVALID 10

int numLines = 1;
void printToken(const char* tokenType, const char* lexeme);

%}

/*Regexes*/
WHITESPACE [ \t\r]+
NEWLINE \n
DIGIT [0-9]
LETTER [a-zA-Z]
SCI [E]
INVALID [^\s]

IF if
ELSE else
FUNC func
LET let
WHILE while

ADD \+
SUB \-
MULT \*
DIV \/
DOT \.

LPAREN [(]
RPAREN [)]

SCICONST {DIGIT}+{DOT}{DIGIT}+{SCI}{DIGIT}+
DECCONST ({SUB}|{ADD})?{DIGIT}+{DOT}{DIGIT}+
IDENT {LETTER}({LETTER}|{DIGIT})*
INTCONST ({SUB}|{ADD})?{DIGIT}+
COMMENT %+(.)*
STRCONST (\"(.)*\")|(\'(.)*\')


%%

{SCICONST}  {
              printToken("SCICONST", yytext);
              return T_SCICONST;
            }

{DECCONST}  {
              printToken("DECCONST", yytext);
              return T_DECCONST;
            }

{STRCONST}  {
              printToken("STRCONST", yytext);
              return T_STRCONST;
            }

{ADD}       {
              printToken("OPERATOR", yytext);
              return T_OPERATOR;
            }

{SUB}       {
              printToken("OPERATOR", yytext);
              return T_OPERATOR;
            }

{MULT}      {
              printToken("OPERATOR", yytext);
              return T_OPERATOR;
            }

{DIV}       {
              printToken("OPERATOR", yytext);
              return T_OPERATOR;
            }

{IF}        {
              printToken("KEYWORD", yytext);
              return T_KEYWORD;
            }

{ELSE}      {
              printToken("KEYWORD", yytext);
              return T_KEYWORD;
            }

{FUNC}      {
              printToken("KEYWORD", yytext);
              return T_KEYWORD;
            }

{LET}       {
              printToken("KEYWORD", yytext);
              return T_KEYWORD;
            }

{WHILE}     {
              printToken("KEYWORD", yytext);
              return T_KEYWORD;
            }

{INTCONST}  {
              printToken("INTCONST", yytext);
              return T_INTCONST;
            }

{IDENT}     {
              printToken("IDENT", yytext);
              return T_IDENT;
            }

{COMMENT}   {}

{WHITESPACE}{}

{NEWLINE}   {numLines += 1;}

{INVALID}   {
              printToken("?", yytext);
              return T_INVALID;
            }

%%

void printToken(const char* tokenType, const char* lexeme)
{
  printf("TOKEN: %s\t LEXEME: %s\n", tokenType, lexeme);
}

//You should specify the yywrap function.
int yywrap() {return 1;}

int main()
{
  while (yylex());
  printf("Processed %d lines\n", numLines);
  return 0;
}
