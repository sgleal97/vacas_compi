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
    if(val=="cadena"):
        procesar_asignacion_cadena(instr, ts)
    elif(val=="logicabinaria"):
        procesar_asignacion_logica(instr,ts)
    elif(val=="logicaunitaria"):
        procesar_asignacion_logica_unitaria(instr,ts)
    elif(val == "bitbinaria"):
        procesar_asignacion_bit(instr,ts)
    elif(val == "bitunitaria"):
        procesar_asignacion_bit_unitaria(instr, ts)
    elif(val == "relacionalbinaria"):
        procesar_asignacion_relacional(instr, ts)
    else:
        flag = ts.buscar(instr.id)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
        if(flag == True):
            ts.actualizar(simbolo)
        else:
            procesar_definicion(instr, ts)
            ts.actualizar(simbolo)

def procesar_definicion_cadena(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, "")
    ts.agregar(simbolo)

def procesar_asignacion_cadena(instr, ts):
    val = resolver_cadena(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_cadena(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_logica(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
    ts.agregar(simbolo)

def procesar_asignacion_logica(instr, ts):
    val = resolver_expresion_binaria_logica(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_logica(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_logica_unitaria(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
    ts.agregar(simbolo)

def procesar_asignacion_logica_unitaria(instr, ts):
    val = resolver_expresion_unitaria_logica(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_logica(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_bit(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, 0)
    ts.agregar(simbolo)

def procesar_asignacion_bit(instr, ts):
    val = resolver_expresion_binaria_bit(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_bit(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_bit_unitaria(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, 0)
    ts.agregar(simbolo)

def procesar_asignacion_bit_unitaria(instr,ts):
    val = resolver_expresion_unitaria_bit(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_bit(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_relacional(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
    ts.agregar(simbolo)

def procesar_asignacion_relacional(instr, ts):
    val = resolver_expresion_binaria_relacional(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_relacional(instr,ts)
        ts.agregar(simbolo)

def resolver_cadena(expCad, ts) :
    #if isinstance(expCad, ExpresionConcatenar) :
    #    exp1 = resolver_cadena(expCad.exp1, ts)
    #    exp2 = resolver_cadena(expCad.exp2, ts)
    #    return exp1 + exp2
    if isinstance(expCad, ExpresionString):
        print (expCad.val," <-AQUI ESTA EL VALOR")
        return expCad.val
    #elif isinstance(expCad, ExpresionCadenaNumerico) :
    #    return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')

def resolver_expresion_binaria_logica(expLog, ts) :
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    print(expLog.exp1,"----",expLog.exp2)
    #Expresiones logicas, True = 1, False = 0; Si el valor es distinto ERROR solo puede retornar 0 o 1
    if expLog.operador == OPERACION_LOGICA.AND :
        if (exp1 == 1 or exp1==0) and (exp2 == 1 or exp2==0):
            return exp1 and exp2
        else:
            print("error AND-",exp1,"-",exp2)
    elif expLog.operador == OPERACION_LOGICA.OR :
        if (exp1 == 1 or exp1==0) and (exp2 == 1 or exp2==0):
            return exp1 or exp2
        else:
            print("error OR-",exp1,"-",exp2)
    elif expLog.operador == OPERACION_LOGICA.XOR :
        if (exp1 == 1 or exp1==0) and (exp2 == 1 or exp2==0):
            return exp1 ^ exp2
        else:
            print("error xor-",exp1,"-",exp2)
    else:
        print("Error: datos no booleanos")

def resolver_expresion_unitaria_logica(expLog, ts):
    exp = resolver_expresion_aritmetica(expLog.exp, ts)
    if exp == 1:
        return 0
    elif exp == 0:
        return 1
    else:
        print("Error: LogicaUnitaria numero")

def resolver_expresion_binaria_bit(expBit, ts):
    exp1 = resolver_expresion_aritmetica(expBit.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expBit.exp2, ts)
    if type(exp1) == int and type(exp2) == int:
        if expBit.operador == OPERACION_BIT.BAND :
            return exp1 & exp2
        elif expBit.operador == OPERACION_BIT.BOR :
            return exp1| exp2
        elif expBit.operador == OPERACION_BIT.BXOR :
            return exp1 ^ exp2
        elif expBit.operador == OPERACION_BIT.SHIFTI:
            return exp1 << exp2
        elif expBit.operador == OPERACION_BIT.SHIFTD:
            return exp1 >> exp2
    else:
        print("Error bit a bit: tipo de dato no entero")

def resolver_expresion_unitaria_bit(expBit, ts):
    exp = resolver_expresion_aritmetica(expBit.exp,ts)
    if type(exp) == int:
        return ~exp
    else:
        print("Error: tipo de dato no int")

def resolver_expresion_binaria_relacional(expRel, ts):
    exp1 = resolver_expresion_aritmetica(expRel.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expRel.exp2, ts)
    #Expresiones relacionales, True = 1, False = 0; Si el valor es distinto ERROR solo puede retornar 0 o 1
    if expRel.operador == OPERACION_RELACIONAL.IGUAL :
        if exp1 == exp2:
            return 1
        else:
            return 0
    elif expRel.operador == OPERACION_RELACIONAL.DIFERENTE :
        if exp1 != exp2:
            return 1
        else:
            return 0
    elif expRel.operador == OPERACION_RELACIONAL.MAYOR_QUE :
        if exp1 > exp2:
            return 1
        else:
            return 0
    elif expRel.operador == OPERACION_RELACIONAL.MENOR_QUE:
        if exp1 < exp2:
            return 1
        else:
            return 0
    elif expRel.operador == OPERACION_RELACIONAL.MAYORIGUAL_QUE:
        if exp1 >= exp2:
            return 1
        else:
            return 0
    elif expRel.operador == OPERACION_RELACIONAL.MENORIGUAL_QUE:
        if exp1 <= exp2:
            return 1
        else:
            return 0
    else:
        print("Error: expresion realacional")


def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.RESIDUO : return exp1 % exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNotLogica):
        return "logicaunitaria"
    elif isinstance(expNum, ExpresionNotBit):
        return "bitunitaria"
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor
    elif isinstance(expNum, ExpresionAbsoluto):
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return abs(exp)
    elif isinstance(expNum, ExpresionString) :
        return "cadena"
    elif isinstance(expNum, ExpresionBinariaLogica):
        return "logicabinaria"
    elif isinstance(expNum, ExpresionBinariaBit):
        return "bitbinaria"
    elif isinstance(expNum, ExpresionBinariaRelacional):
        return "relacionalbinaria"

def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones:
        #if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
        #elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
        if isinstance(instr, Asignacion):
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
        print(">> ID: ", ts_global.simbolos[x].id,
         " VALOR: ", ts_global.simbolos[x].valor,
         " TIPO: ", ts_global.simbolos[x].tipo.value
        )
    #    #
    print(">>>>>>>>>>>>>>>>>>>>>>>")

