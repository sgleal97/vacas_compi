import gramatica as g
import ts as TS
import interfaz as inter
from expresiones import *
from instrucciones import *

def procesar_definicion(instr, ts) :
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)      # inicializamos con 0 como valor por defecto
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion(instr, ts)
        procesar_asignacion(instr, ts)

def resolver_cadena(expCad, ts) :
    #if isinstance(expCad, ExpresionConcatenar) :
    #    exp1 = resolver_cadena(expCad.exp1, ts)
    #    exp2 = resolver_cadena(expCad.exp2, ts)
    #    return exp1 + exp2
    if isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    #elif isinstance(expCad, ExpresionCadenaNumerico) :
    #    return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor

def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones:
        #if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
        #elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
        if isinstance(instr, Asignacion) : 
            print("asignacion")
            procesar_asignacion(instr, ts)
        #elif isinstance(instr, Mientras) : procesar_mientras(instr, ts)
        #elif isinstance(instr, If) : procesar_if(instr, ts)
        #elif isinstance(instr, IfElse) : procesar_if_else(instr, ts)
        else : print('Error: instrucción no válida')


def Main(input):
    #print('main')
    #print(input)
    instrucciones = g.parse(input)
    ts_global = TS.TablaDeSimbolos()

    procesar_instrucciones(instrucciones,ts_global)
    print(">>>>>>>>>>>>>>>>>>>>>>>")
    for x in ts_global.simbolos:
        print(">> ID: ", ts_global.simbolos[x].id
        + " VALOR: ", ts_global.simbolos[x].valor
        )
    #    #+ " TIPO: "+ ts_global.simbolos[x].tipo
    print(">>>>>>>>>>>>>>>>>>>>>>>")

