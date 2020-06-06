reserved = {
    'main' : 'MAIN',
    'goto' : 'GOTO',
    'unset' : 'UNSET',
    'print' : 'PRINT',
    'read' : 'READ',
    'abs' : 'ABS',
    'exit' : 'EXIT',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'if' : 'IF'
}

tokens  = [
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
    #'DOLLAR',
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
    'DOSPUNTOS',
    'ID',
    'VAR',
    'CADENA'
] + list(reserved.values())

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
#t_DOLLAR    = r'\$'
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
     t.type = reserved.get(t.value.lower(),'ID')    # Check for reserved words
     return t
    
def t_VAR(t):
    r'[$][a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'VAR')     #Check for reserved words
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

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

import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática

#from prueba import *
from expresiones import *
from instrucciones import *



def p_init(t):
    'init                   : MAIN DOSPUNTOS cuerpo'
    t[0] = t[3]

def p_lista_cuerpo(t):
    'cuerpo                 : instrucciones labels'
    t[1]+=t[2]
    t[0]=t[1]

def p_cuerpo(t):
    'cuerpo                 : labels'
    t[0]=t[1]

def p_lista_label(t):
    'labels                 : labels label'
    t[1]+=t[2]
    t[0]=t[1]

def p_label_instrucion(t):
    'labels                 : label'
    t[0]=t[1]

def p_label(t):
    'label                  : ID DOSPUNTOS instrucciones'
    t[0]=t[3]

def p_lista_instrucciones(t):
    'instrucciones          : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones          : instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion          : asignacion
                            | if_instr
                            '''
    t[0] = t[1]

def p_asignacion(t):
    'asignacion             : VAR IGUAL exp_numerica PTCOMA'
    t[0] = Asignacion(t[1], t[3])

def p_exp_numerica_binaria(t):
    '''exp_numerica         : exp_numerica MAS exp_numerica
                            | exp_numerica MENOS exp_numerica
                            | exp_numerica POR exp_numerica
                            | exp_numerica DIVIDIDO exp_numerica'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

def p_exp_numerica_unaria(t):
    'exp_numerica         : MENOS exp_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_exp_numerica_valores(t):
    '''exp_numerica         : ENTERO
                            | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_exp_id(t):
    'exp_numerica           : VAR'
    t[0] = ExpresionIdentificador(t[1])

def p_exp_cadena(t):
    'exp_numerica           : CADENA'
    t[0] = ExpresionDobleComilla(t[1])

def p_etiqueta(t):
    'etiqueta_instr         : ID DOSPUNTOS'
    t[0] = t[1]

def p_if(t):
    'if_instr               : IF goto_instr'

def p_etiqueta(t):
    'goto_instr             : GOTO ID PTCOMA'
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    #f = open("./entrada.txt", "r")
    #input = f.read()
    #prueba.Content.consola.setPlainText(input)
    #prueba.Content.consola.add()
    print("############")
    print(input)
    print("############")
    return parser.parse(input)