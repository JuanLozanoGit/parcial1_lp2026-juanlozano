%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Declaración para evitar el error de declaración implícita
int yylex();
void yyerror(const char *s);

double newton_sqrt(double n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    double x = n;
    for(int i = 0; i < 10; i++) {
        x = 0.5 * (x + n/x);
    }
    return x;
}
%}

%union {
    float fval;
}

%token <fval> NUM
%token SQRT

%%
input: 
    | input line
    ;

line: 
    SQRT '(' NUM ')' { printf("Resultado NR: %.4f\n", newton_sqrt($3)); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error sintáctico: %s\n", s);
}

int main() {
    return yyparse();
}
