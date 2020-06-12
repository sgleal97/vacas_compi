import ply.lex as lex
import ply.yacc as yacc

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
    'if' : 'IF',
    'xor' : 'XOR',
    'array' : 'ARRAY'
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
t_RESIDUO   = r'\%'
t_PTCOMA    = r';'
t_NOT       = r'!'
t_BNOT      = r'~'
t_BAND      = r'&'
t_BOR       = r'\|'
t_BXOR      = r'\^'
t_AND       = r'&&'
t_OR        = r'\|\|'
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
    global entrada
    print("Illegal character '%s'" % t.value[0])
    Diccionario = {'Error': str(t.value[0]), 'Tipo': 'Lexico', 'Fila': t.lineno, 'Columna': find_column(entrada,t)}
    print(t.value)
    errorLexicos.agregar(Diccionario)
    t.lexer.skip(1)
    
# Construyendo el analizador léxico

lexer = lex.lex()

# Asociación de operadores y precedencia
#nonassoc para que solo permita operaciones simples
#left o right para permitir operaciones complejas
precedence = (
    ('nonassoc', 'OR',),
    ('nonassoc', 'XOR',),
    ('nonassoc', 'AND'),
    ('nonassoc', 'NOT'),
    ('nonassoc', 'BOR',),
    ('nonassoc', 'BXOR',),
    ('nonassoc', 'BAND'),
    ('nonassoc', 'BNOT'),
    ('nonassoc', 'SHIFTI', 'SHIFTD'),
    ('nonassoc', 'IGUALQ', 'NIGUALQ'),
    ('nonassoc', 'MENORQ', 'MAYORQ','MENORIGUALQ','MAYORIGUALQ'),
    ('nonassoc','MAS','MENOS'),
    ('nonassoc','POR','DIVIDIDO', 'RESIDUO'),
    ('nonassoc','UMENOS'),
    )

# Definición de la gramática

#from prueba import *
from expresiones import *
from instrucciones import *
import pila as PILA
import ply.lex as lex

ambito = PILA.Pila()
ambito.push('main')

def p_init(t):
    'init                   : MAIN DOSPUNTOS instrucciones'#instrucciones x cuerpo
    t[0] = t[3]
    print("Ambito: ",ambito.inspeccionar())
#
#def p_lista_cuerpo(t):
#    'cuerpo                 : instrucciones labels'
#    t[1]+=t[2]
#    t[0]=t[1]
#
#def p_cuerpo(t):
#    'cuerpo                 : labels'
#    t[0]=t[1]
#
#def p_lista_label(t):
#    'labels                 : labels label'
#    t[1]+=t[2]
#    t[0]=t[1]
#
#def p_label_instrucion(t):
#    'labels                 : label'
#    t[0]=t[1]
#
#def p_label(t):
#    'label                  : ID DOSPUNTOS instrucciones'
#    t[0]=t[3]
#
def p_lista_instrucciones(t):
    'instrucciones          : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones          : instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion          : asignacion
                            | array_instr
                            | print_instr
                            | unset_instr
                            | if_instr
                            | etiqueta_instr
                            | goto_instr
                            '''
    t[0] = t[1]

def p_array_instr(t):
    'array_instr            : VAR indices IGUAL exp_numerica PTCOMA'
    t[0] = AsignacionPosicionArray(t[1], t[2], t[4], ambito.inspeccionar())

def p_lista_indices(t):
    'indices                : indices indice'
    t[1].append(t[2])
    t[0]=t[1]

def p_indices_indice(t):
    'indices                : indice'
    t[0] = [t[1]]

def p_indice(t):
    'indice                 : CORIZQ exp_numerica CORDER'
    t[0] = t[2]

def p_asignacion(t):
    'asignacion             : VAR IGUAL exp_numerica PTCOMA'
    if t[2] == '=': t[0] = Asignacion(t[1], t[3], ambito.inspeccionar())

def p_exp_numerica_binaria(t):
    '''exp_numerica         : exp_numerica MAS exp_numerica
                            | exp_numerica MENOS exp_numerica
                            | exp_numerica POR exp_numerica
                            | exp_numerica DIVIDIDO exp_numerica
                            | exp_numerica RESIDUO exp_numerica
                            | exp_numerica AND exp_numerica
                            | exp_numerica OR exp_numerica
                            | exp_numerica XOR exp_numerica
                            | exp_numerica BAND exp_numerica
                            | exp_numerica BOR exp_numerica
                            | exp_numerica BXOR exp_numerica
                            | exp_numerica SHIFTI exp_numerica
                            | exp_numerica SHIFTD exp_numerica
                            | exp_numerica IGUALQ exp_numerica
                            | exp_numerica NIGUALQ exp_numerica
                            | exp_numerica MAYORQ exp_numerica
                            | exp_numerica MENORQ exp_numerica
                            | exp_numerica MAYORIGUALQ exp_numerica
                            | exp_numerica MENORIGUALQ exp_numerica
                            | PARIZQ tipo_dato PARDER VAR'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.RESIDUO)
    elif t[2] == '&&': t[0] = ExpresionBinariaLogica(t[1], t[3], OPERACION_LOGICA.AND)
    elif t[2] == '||': t[0] = ExpresionBinariaLogica(t[1], t[3], OPERACION_LOGICA.OR)
    elif t[2] == 'xor': t[0] = ExpresionBinariaLogica(t[1], t[3], OPERACION_LOGICA.XOR)
    elif t[2] == '&': t[0] = ExpresionBinariaBit(t[1], t[3], OPERACION_BIT.BAND)
    elif t[2] == '|': t[0] = ExpresionBinariaBit(t[1], t[3], OPERACION_BIT.BOR)
    elif t[2] == '^': t[0] = ExpresionBinariaBit(t[1], t[3], OPERACION_BIT.BXOR)
    elif t[2] == '<<': t[0] = ExpresionBinariaBit(t[1], t[3], OPERACION_BIT.SHIFTI)
    elif t[2] == '>>': t[0] = ExpresionBinariaBit(t[1], t[3], OPERACION_BIT.SHIFTD)
    elif t[2] == '==': t[0] = ExpresionBinariaRelacional(t[1], t[3], OPERACION_RELACIONAL.IGUAL)
    elif t[2] == '!=': t[0] = ExpresionBinariaRelacional(t[1], t[3], OPERACION_RELACIONAL.DIFERENTE)
    elif t[2] == '>=': t[0] = ExpresionBinariaRelacional(t[1], t[3], OPERACION_RELACIONAL.MAYORIGUAL_QUE)
    elif t[2] == '<=': t[0] = ExpresionBinariaRelacional(t[1], t[3], OPERACION_RELACIONAL.MENORIGUAL_QUE)
    elif t[2] == '>': t[0] = ExpresionBinariaRelacional(t[1], t[3], OPERACION_RELACIONAL.MAYOR_QUE)
    elif t[2] == '<': t[0] = ExpresionBinariaRelacional(t[1], t[3], OPERACION_RELACIONAL.MENOR_QUE)
    elif t[2] == 'int': t[0] = ExpresionConversion(t[2], t[4])
    elif t[2] == 'float': t[0] = ExpresionConversion(t[2], t[4])
    elif t[2] == 'char': t[0] = ExpresionConversion(t[2], t[4])
    

def p_exp_numerica_unaria(t):
    '''exp_numerica         : MENOS exp_numerica %prec UMENOS
                            | NOT exp_numerica %prec UMENOS
                            | BNOT exp_numerica %prec UMENOS'''
    if t[1] == '-': t[0] = ExpresionNegativo(t[2])
    elif t[1] == '!': t[0] = ExpresionNotLogica(t[2])
    elif t[1] == '~': t[0] = ExpresionNotBit(t[2])
    
def p_exp_numerica_abs(t):
    'exp_numerica           : ABS PARIZQ exp_numerica PARDER'
    t[0] = ExpresionAbsoluto(t[3])

def p_exp_numerica_valores(t):
    '''exp_numerica         : ENTERO
                            | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_exp_id(t):
    '''exp_numerica         : VAR
                            | VAR indices'''
    try:
        t[0] = ExpresionArray(t[1], t[2])
    except:
        t[0] = ExpresionIdentificador(t[1])

def p_exp_cadena(t):
    'exp_numerica           : CADENA'
    t[0] = ExpresionString(t[1])

def p_exp_array(t):
    'exp_numerica           : ARRAY PARIZQ PARDER'
    t[0] = ExpresionDeclaracionArray("array()")

def p_tipo_dato(t):
    '''tipo_dato            : INT
                            | FLOAT
                            | CHAR'''
    t[0]=t[1]

def p_print(t):
    'print_instr            : PRINT PARIZQ exp_numerica PARDER PTCOMA'
    t[0] = Imprimir(t[3])

def p_unset(t):
    'unset_instr            : UNSET PARIZQ exp_numerica PARDER PTCOMA'
    t[0] = Unset(t[3])

def p_if(t):
    'if_instr               : IF PARIZQ exp_numerica PARDER goto_instr'
    t[0] = If(t[3], t[5])

def p_etiqueta(t):
    'etiqueta_instr         : ID DOSPUNTOS'
    if ambito.size() == 1:
        ambito.push(t[1])
    else:
        ambito.pop()
        ambito.push(t[1])
    t[0] = Etiqueta(t[1])

def p_goto(t):
    'goto_instr             : GOTO ID PTCOMA'
    t[0] = Goto(t[2])

def p_error(p):
    global entrada
    if p:
        print("Syntax error at token", p.type, "Fila: ", p.lineno+1, "Columna: ", find_column(entrada,p), "Valor: ", format(p.value))
        Diccionario = {'Error': p.value, 'Tipo': 'Sintactico', 'Fila': p.lineno, 'Columna': find_column(entrada,p)}
        errorLexicos.agregar(Diccionario)
        # Just discard the token and tell the parser it's okay..
        parser.errok()
    else:
        print("Syntax error at EOF")

'''METODO CON AYUDA DEL AUX
def p_error(t):
    global entrada
    global parser
    tok = parser.token()
    while True:
        if tok is not None:
            if tok.value == ';':
                print('here')
                break
            tok = parser.token()
            print(tok.value)
        else:
            break
    print('sale')
    return tok.type
'''
''' METODO DE LA DOCUMENTACION DE PLY
def p_error(p):
    global entrada
    global parser
    # Read ahead looking for a terminating ";"
    print(p)
    while True:
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PTCOMA': break
    parser.errok()

    # Return SEMI to the parser as the next lookahead token
    return tok  
'''

parser = yacc.yacc()
errorLexicos = PILA.Pila()
erroresSintacticos = PILA.Pila()

def parse(input):
    global entrada
    entrada = input
    #f = open("./entrada.txt", "r")
    #input = f.read()
    #prueba.Content.consola.setPlainText(input)
    #prueba.Content.consola.add()
    print("############")
    print(input)
    print("############")
    return parser.parse(input)

entrada = ""