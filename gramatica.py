reservadas = {
    'main'  : 'MAIN',
    'goto'  : 'GOTO',
    'unset' : 'UNSET',
    'print' : 'PRINT',
    'read'  : 'READ',
    'abs'   : 'ABS',
    'exit'  : 'EXIT'
}

tokens  = (
    'REVALUAR',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'RESIDUO',
    'DECIMAL',
    'ENTERO',
    'PTCOMA',
    'DOLLAR',
    'NOT',
    'AND',
    'OR',
    'XOR',
    'BNOT',
    'BAND',
    'BOR',
    'BXOR',
    'SHIFTD',
    'SHIFTI',
    'IGUAL',
    'MENORQ',
    'MAYORQ',
    'IGUALQ',
    'NIGUALQ',
    'MAYORIGUALQ',
    'MENORIGUALQ',
    'DOSPUNTOS'

)

# Tokens
t_REVALUAR  = r'Evaluar'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_RESIDUO   = r'%'
t_PTCOMA    = r';'
t_DOLLAR    = r'\$'
t_NOT       = r'!'
t_BNOT      = r'~'
t_BAND      = r'&'
t_BOR       = r'\|'
t_BXOR      = r'\^'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_XOR       = r'xor'
t_MENORQ    = r'<'
t_MAYORQ    = r'>'
t_SHIFTD    = r'>>'
t_SHIFTI    = r'<<'
t_IGUAL     = r'='
t_IGUALQ    = r'=='
t_NIGUALQ   = r'!='
t_MENORIGUALQ = r'<='
t_MAYORIGUALQ = r'>='
t_DOSPUNTOS   = r':'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
    #r'[$][a-zA-Z_0-9]*
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
import prueba
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''

def p_instrucciones_evaluar(t):
    'instruccion : REVALUAR CORIZQ expresion CORDER PTCOMA'
    print('El valor de la expresión es: ' + str(t[3]))

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL'''
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def correr(input):
    #f = open("./entrada.txt", "r")
    #input = f.read()
    #prueba.Content.consola.setPlainText(input)
    #prueba.Content.consola.add()
    parser.parse(input)