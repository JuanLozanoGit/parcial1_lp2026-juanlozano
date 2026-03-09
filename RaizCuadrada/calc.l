%{
#include "calc.tab.h"
#include <stdlib.h>
%}

%%
"SQRT"          { return SQRT; }
[0-9]+(\.[0-9]+)? { yylval.fval = atof(yytext); return NUM; }
"("             { return '('; }
")"             { return ')'; }
[ \t\n]         ;
.               { return yytext[0]; }
%%

int yywrap() {
    return 1;
}
