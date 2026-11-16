grammar Grammar;

// Головне правило: вираз завершується кінцем рядка
expressionRoot
    : expression EOF
    ;

// Усі можливі вирази з урахуванням пріоритетів операторів
expression
    : '(' expression ')'                          # parenExpr
    | MMAX '(' expression (',' expression)* ')'   # mmaxExpr
    | MMIN '(' expression (',' expression)* ')'   # mminExpr
    | CELL                                        # cellRefExpr
    | '+' expression                              # plusExpr
    | '-' expression                              # minusExpr
    | expression '*' expression                   # multExpr
    | expression '/' expression                   # divExpr
    | expression DIV expression                   # divFuncExpr
    | expression MOD expression                   # modExpr
    | expression '+' expression                   # addExpr
    | expression '-' expression                   # subExpr
    | INT                                         # numberExpr
    ;

// Лексичні правила (токени)
MMAX: [mM][mM][aA][xX];
MMIN: [mM][mM][iI][nN];
DIV: [dD][iI][vV];
MOD: [mM][oO][dD];

// Посилання на клітинку: одна або дві букви латиниці (A-Z) + ціле число (1-999...)
CELL
    : [A-Za-z]+ [0-9]+
    ;

// Ціле число довільної довжини
INT
    : [0-9]+
    ;

// Пробіли та табуляції ігноруються
WS
    : [ \t\r\n]+ -> skip
    ;