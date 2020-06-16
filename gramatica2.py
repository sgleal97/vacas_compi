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
    r'\".*?\"|\'.*?\''
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
    global input
    print("Illegal character '%s'" % t.value[0])
    Diccionario = {'Error': str(t.value[0]), 'Tipo': 'Lexico', 'Fila': t.lineno, 'Columna': find_column(input,t)}
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
    #('nonassoc','UMENOS'),
    )

# Definición de la gramática

#from prueba import *
from expresiones import *
from instrucciones import *
import pila as PILA

ambito = PILA.Pila()
simulador = PILA.Pila()
instrucciones = PILA.Pila()
ambito.push('main')


def p_init(t):
    'init                   : MAIN DOSPUNTOS instrucciones'
    t[0] = t[3]
    print(t[0])
    
def p_lista_instrucciones(t):
    'instrucciones          : instruccion instrucciones2'
    if t[2]=="vacio":
        t[0] = [t[1]]
    else:
        t[2].append(t[1])
        t[0] = t[2]

def p_instrucciones_instruccion(t):
    'instrucciones2         : instruccion instrucciones2'
    if t[2]=="vacio":
        t[0] = [t[1]]
    else:
        t[2].append(t[1])
        t[0] = t[2]

def p_instrucciones_instruccion2(t):
    'instrucciones2         : empty'
    t[0] = "vacio"
    Diccionario = {'produccion': 'indices2', 'regla':'empty', 'semantica':'instrucciones2.sin=instrucciones2.sin'}
    reporteGramatical.push(Diccionario)

def p_instruccion_asignacion(t):
    'instruccion            : asignacion'
    Diccionario = {'produccion': 'instruccion', 'regla':'asignacion', 'semantica':'instruccion.val = asignacion.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_array(t):
    'instruccion            : array_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'array_instr', 'semantica':'instruccion.val = array_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_unset(t):
    'instruccion            : unset_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'unset_instr', 'semantica':'instruccion.val = unset_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_print(t):
    'instruccion            : print_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'print_instr', 'semantica':'instruccion.val = print_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_if(t):
    'instruccion            : if_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'if_instr', 'semantica':'instruccion.val = if_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_etiqueta(t):
    'instruccion            : etiqueta_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'etiqueta_instr', 'semantica':'instruccion.val = etiqueta_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_goto(t):
    'instruccion            : goto_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'goto_instr', 'semantica':'instruccion.val = goto_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_instruccion_exit(t):
    'instruccion             : exit_instr'
    Diccionario = {'produccion': 'instruccion', 'regla':'exit_instr', 'semantica':'instruccion.val = exit_instr.val'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_asignacion(t):
    '''asignacion           : VAR IGUAL exp_numerica PTCOMA
                            | VAR IGUAL READ PARIZQ  PARDER PTCOMA
                            | VAR IGUAL BAND VAR PTCOMA'''
    if t[3] == 'read':
        t[0] = Read(t[1], 0)
        Diccionario = {'produccion': 'asignacion', 'regla':'VAR IGUAL READ PARIZQ PARDER PTCOMA', 'semantica':'asignacion.val = Asignacion(VAR.val, exp_numerica.val)'}
        reporteGramatical.push(Diccionario)
    elif t[3] == '&':
        Diccionario = {'produccion': 'asignacion', 'regla':'VAR IGUAL BAND VAR', 'semantica':'Asignacion.val = ExpresionApuntador(VAR1.val, VAR2.val)'}
        reporteGramatical.push(Diccionario)
        t[0] = ExpresionApuntador(t[1], t[4])#ARREGLAR
    else:
        Diccionario = {'produccion': 'asignacion', 'regla':'VAR IGUAL exp_numerica PTCOMA', 'semantica':'asignacion.val = Asignacion(VAR.val, exp_numerica.val)'}
        reporteGramatical.push(Diccionario)
        t[0] = Asignacion(t[1], t[3], ambito.inspeccionar())
    

def p_array(t):
    'array_instr            : VAR indices IGUAL exp_numerica PTCOMA'
    Diccionario = {'produccion': 'array_instr', 'regla':'VAR indices IGUAL exp_numerica PTCOMA', 
                                'semantica':'array_instr.val=AsignacionPosicionArray(VAR.val, indices.val, exp_numerica.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = AsignacionPosicionArray(t[1], t[2], t[4], ambito.inspeccionar())

def p_imprimir(t):
    'print_instr            : PRINT PARIZQ exp_numerica PARDER PTCOMA'
    Diccionario = {'produccion': 'print_instr', 'regla':'PRINT PARIZQ exp_numerica PARDER PTCOMA', 'semantica':'print_instr.val = Imprimir(exp_numerica.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = Imprimir(t[3])

def p_unset(t):
    'unset_instr            : UNSET PARIZQ exp_numerica PARDER PTCOMA'
    Diccionario = {'produccion': 'unset_instr', 'regla':'UNSET PARIZQ exp_numerica PARDER PTCOMA', 'semantica':'unset_instr.val = Unset(exp_numerica.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = Unset(t[3])

def p_if(t):
    'if_instr               : IF PARIZQ exp_numerica PARDER goto_instr'
    Diccionario = {'produccion': 'if_instr', 'regla':'IF PARIZQ exp_numerica PARDER goto_instr', 'semantica':'if_instr.val = If(exp_numerica.val, goto_instr.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = If(t[3], t[5])
    
def p_etiqueta(t):
    'etiqueta_instr         : ID DOSPUNTOS'
    Diccionario = {'produccion': 'etiqueta_instr', 'regla':'ID DOSPUNTOS', 'semantica':'etiqueta_instr.val = ambito(ID)'}
    reporteGramatical.push(Diccionario)
    if ambito.size() == 1:
        ambito.push(t[1])
    else:
        ambito.pop()
        ambito.push(t[1])
    t[0] = Etiqueta(t[1])

def p_goto(t):
    'goto_instr             : GOTO ID PTCOMA'
    Diccionario = {'produccion': 'goto_instr', 'regla':'GOTO ID PTCOMA', 'semantica':'goto_instr.val = Goto(ID)'}
    reporteGramatical.push(Diccionario)
    t[0] = Goto(t[2])

def p_exit(t):
    'exit_instr             : EXIT PTCOMA'
    Diccionario = {'produccion': 'exit_instr', 'regla':'EXIT PTCOMA', 'semantica':'exit_instr.val = Exit(EXIT)'}
    reporteGramatical.push(Diccionario)
    t[0] = Exit("Exit")

def p_expresion(t):
    'exp_numerica           : valores exp_numerica2'
    auxiliar = simulador.pop()
    if(auxiliar == "vacio"):
        print("exp_numerica", "=", str(t[1]))
        t[0] = t[1]
    else:
        print("exp_numerica", "=", str(t[1]), str(t[2]), auxiliar)
        ####
        if t[2] == '+'  : 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica MAS exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, MAS)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinaria(t[1], auxiliar, OPERACION_ARITMETICA.MAS)
        elif t[2] == '-': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica MENOS exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, MENOS)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinaria(t[1], auxiliar, OPERACION_ARITMETICA.MENOS)
        elif t[2] == '*': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica POR exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, POR)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinaria(t[1], auxiliar, OPERACION_ARITMETICA.POR)
        elif t[2] == '/': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica DIVIDIDO exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, DIVIDIDO)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinaria(t[1], auxiliar, OPERACION_ARITMETICA.DIVIDIDO)
        elif t[2] == '%': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica RESIDUO exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, RESIDUO)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinaria(t[1], auxiliar, OPERACION_ARITMETICA.RESIDUO)
        elif t[2] == '&&': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica AND exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, AND)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaLogica(t[1], auxiliar, OPERACION_LOGICA.AND)
        elif t[2] == '||': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica OR exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, OR)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaLogica(t[1], auxiliar, OPERACION_LOGICA.OR)
        elif t[2] == 'xor': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica XOR exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, XOR)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaLogica(t[1], auxiliar, OPERACION_LOGICA.XOR)
        elif t[2] == '&': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica BAND exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, BAND)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaBit(t[1], auxiliar, OPERACION_BIT.BAND)
        elif t[2] == '|': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica BOR exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, BOR)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaBit(t[1], auxiliar, OPERACION_BIT.BOR)
        elif t[2] == '^': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica BXOR exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, BXOR)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaBit(t[1], auxiliar, OPERACION_BIT.BXOR)
        elif t[2] == '<<': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica SHIFTI exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, SHIFTI)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaBit(t[1], auxiliar, OPERACION_BIT.SHIFTI)
        elif t[2] == '>>': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica SHIFTI exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, SHIFTD)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaBit(t[1], auxiliar, OPERACION_BIT.SHIFTD)
        elif t[2] == '==': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica IGUALQ exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, IGUAL)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaRelacional(t[1], auxiliar, OPERACION_RELACIONAL.IGUAL)
        elif t[2] == '!=': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica NIGUALQ exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, DIFERENTE)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaRelacional(t[1], auxiliar, OPERACION_RELACIONAL.DIFERENTE)
        elif t[2] == '>=': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica MENOIGUALRQUE exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, MENORRIQUALQUE)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaRelacional(t[1], auxiliar, OPERACION_RELACIONAL.MAYORIGUAL_QUE)
        elif t[2] == '<=': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica MAYORIGUALQUE exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, MAYORIGUALQUE)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaRelacional(t[1], auxiliar, OPERACION_RELACIONAL.MENORIGUAL_QUE)
        elif t[2] == '>': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica MENORQUE exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, MAYORQUE)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaRelacional(t[1], auxiliar, OPERACION_RELACIONAL.MAYOR_QUE)
        elif t[2] == '<': 
            Diccionario = {'produccion': 'exp_numerica', 'regla':'exp_numerica MAYORQUE exp_numerica', 'semantica':'exp_numerica.val = ExpresionBinaria(valores.val, exp_numerica2.val, MENORQUE)'}
            reporteGramatical.push(Diccionario)
            t[0] = ExpresionBinariaRelacional(t[1], auxiliar, OPERACION_RELACIONAL.MENOR_QUE)
        ###
        

def p_expresion_unaria(t):
    '''exp_numerica         : BNOT valores
                            | MENOS valores
                            | NOT valores'''
    if t[1] == '-': 
        Diccionario = {'produccion': 'exp_numerica', 'regla':'MENOS', 'semantica':'exp_numerica.val = ExpresionNegativo(valores.val)'}
        reporteGramatical.push(Diccionario)
        t[0] = ExpresionNegativo(t[2])
    elif t[1] == '!': 
        t[0] = ExpresionNotLogica(t[2])
        Diccionario = {'produccion': 'exp_numerica', 'regla':'NOT', 'semantica':'exp_numerica.val = ExpresionNotLogica(valores.val)'}
        reporteGramatical.push(Diccionario)
    elif t[1] == '~': 
        t[0] = ExpresionNotBit(t[2])
        Diccionario = {'produccion': 'exp_numerica', 'regla':'BNOT', 'semantica':'exp_numerica.val = ExpresionNotBit(valores.val)'}
        reporteGramatical.push(Diccionario)

def p_expresion_array(t):
    'exp_numerica           : ARRAY PARIZQ PARDER'
    Diccionario = {'produccion': 'exp_numerica', 'regla':'ARRAY PARIZQ PARDER', 'semantica':'exp_numerica.val = ExpresionDeclaracionArray(ARRAY.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = ExpresionDeclaracionArray("array()")

def p_expresion_unaria_abs(t):
    'exp_numerica           : ABS PARIZQ valores PARDER'
    Diccionario = {'produccion': 'exp_numerica', 'regla':'ABS PARIZQ exp_numerica PARDER', 'semantica':'exp_numerica.val = ExpresionAbsoluto(valores.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = ExpresionAbsoluto(t[3])

def p_expresion_conversion(t):
    'exp_numerica           : PARIZQ tipo_dato PARDER VAR'
    if t[2] == 'int': 
        Diccionario = {'produccion': 'exp_numerica', 'regla':'PARIZQ tipo_dato PARDER VAR', 'semantica':'exp_numerica.val = EXpresionConversion(tipo_dato.val, INT)'}
        reporteGramatical.push(Diccionario)
        t[0] = ExpresionConversion(t[2], t[4])
    elif t[2] == 'float': 
        Diccionario = {'produccion': 'exp_numerica', 'regla':'PARIZQ tipo_dato PARDER VAR', 'semantica':'exp_numerica.val = ExpresionConversion(tipo_dato.val, FLOAT)'}
        reporteGramatical.push(Diccionario)
        t[0] = ExpresionConversion(t[2], t[4])
    elif t[2] == 'char': 
        Diccionario = {'produccion': 'exp_numerica', 'regla':'PARIZQ tipo_dato PARDER VAR', 'semantica':'exp_numerica.val = ExpresionConversion(tipo_dato.val, CHAR)'}
        reporteGramatical.push(Diccionario)
        t[0] = ExpresionConversion(t[2], t[4])

def p_expresion2(t):
    'exp_numerica2          : signo valores'
    t[0] = t[1]
    simulador.push(t[2])

def p_expresion2_2(t):
    'exp_numerica2          : empty'
    t[0] = t[-1]
    simulador.push("vacio")

def p_lista_indices(t):
    'indices                : indice indices2'
    if t[2]=="vacio":
        t[0] = [t[1]]
        Diccionario = {'produccion': 'indices', 'regla':'indice indices', 'semantica':'indices=indice'}
        reporteGramatical.push(Diccionario)
    else:
        t[2].append(t[1])
        t[0] = t[2]
        Diccionario = {'produccion': 'indices', 'regla':'indice indices', 'semantica':'indices=indice.append(indice2)'}
        reporteGramatical.push(Diccionario)

def p_indices_indice(t):
    'indices2               : indice indices2'
    if t[2]=="vacio":
        t[0] = [t[1]]
        Diccionario = {'produccion': 'indices2', 'regla':'indice indices', 'semantica':'indices2=indice'}
        reporteGramatical.push(Diccionario)
    else:
        t[2].append(t[1])
        t[0] = t[2]
        Diccionario = {'produccion': 'indices2', 'regla':'indice indices', 'semantica':'indices=indice.append(indice2)'}
        reporteGramatical.push(Diccionario)

def p_indices_indice2(t):
    'indices2               : empty'
    Diccionario = {'produccion': 'indices2', 'regla':'empty', 'semantica':'indices.sin=indices2.sin'}
    reporteGramatical.push(Diccionario)
    t[0] = "vacio"

def p_indice(t):
    'indice                 : CORIZQ exp_numerica CORDER'
    Diccionario = {'produccion': 'indice', 'regla':'CORIZQ exp_numerica CORDER', 'semantica':'indice = exp_numerica'}
    reporteGramatical.push(Diccionario)
    t[0] = t[2]

def p_valor_entero(t):
    'valores          : ENTERO'
    Diccionario = {'produccion': 'valores', 'regla':'ENTERO', 'semantica':'exp_numerica.val = ExpresionNumero(ENTERO)'}
    reporteGramatical.push(Diccionario)
    t[0] = ExpresionNumero(t[1])

def p_valor_decimal(t):
    'valores           : DECIMAL'
    Diccionario = {'produccion': 'valores', 'regla':'DECIMAL', 'semantica':'exp_numerica.val = ExpresionNumero(DECIMAL)'}
    reporteGramatical.push(Diccionario)
    t[0] = ExpresionNumero(t[1])

def p_valor_var(t):
    'valores                : VAR'
    t[0] = ExpresionIdentificador(t[1])
    Diccionario = {'produccion': 'goto_instr', 'regla':'VAR', 'semantica':'exp_numerica.val = ExpresionIdentificador(VAR.val)'}
    reporteGramatical.push(Diccionario)

def p_valor_var_indices(t):
    'valores                : VAR indices'
    t[0] = ExpresionArray(t[1], t[2])
    Diccionario = {'produccion': 'exp_numerica', 'regla':'VAR indices', 'semantica':'exp_numerica.val = ExpresionArray(VAR.val, indices.val)'}
    reporteGramatical.push(Diccionario)

def p_valor_cadena(t):
    'valores                : CADENA'
    Diccionario = {'produccion': 'exp_numerica', 'regla':'CADENA', 'semantica':'exp_numerica.val = ExpresionString(CADENA.val)'}
    reporteGramatical.push(Diccionario)
    t[0] = ExpresionString(t[1])

def p_signo(t):
    '''signo                : MAS
                            | MENOS
                            | POR
                            | DIVIDIDO
                            | RESIDUO
                            | AND
                            | OR
                            | XOR
                            | BAND
                            | BOR
                            | BXOR
                            | SHIFTI
                            | SHIFTD
                            | IGUALQ
                            | NIGUALQ
                            | MAYORQ
                            | MENORQ
                            | MAYORIGUALQ
                            | MENORIGUALQ'''
    t[0] = t[1]

def p_tipo_dato_int(t):
    'tipo_dato              : INT'
    Diccionario = {'produccion': 'tipo_dato', 'regla':'INT', 'semantica':'tipo_dato.val = INT'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_tipo_dato_float(t):
    'tipo_dato              : FLOAT'
    Diccionario = {'produccion': 'exp_numerica', 'regla':'FLOAT', 'semantica':'tipo_dato.val = FLOAT'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]

def p_tipo_dato_char(t):
    'tipo_dato              : CHAR'
    Diccionario = {'produccion': 'tipo_dato', 'regla':'CHAR', 'semantica':'tipo_dato.val = CHAR'}
    reporteGramatical.push(Diccionario)
    t[0] = t[1]
    
def p_empty(t):
    'empty                  :'
    Diccionario = {'produccion': 'empty', 'regla':'e', 'semantica':'empty.her=indices2.sin'}
    reporteGramatical.push(Diccionario)

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

parser = yacc.yacc()
errorLexicos = PILA.Pila()
erroresSintacticos = PILA.Pila()
reporteGramatical = PILA.Pila()

def parse(entrada):
    global input
    input = entrada
    print("############    DESCENDENTE      #############")
    print(input)
    print("############    DESCENDENTE      ############")
    return parser.parse(input)

input = ""