import gramatica as g
import ts as TS
from interfaz import *
from expresiones import *
from instrucciones import *
import pila as PILA
import copy
import collections
import time

def update(dict1, dict2):
    for key, value in dict2.items():
        if value and isinstance(value, collections.Mapping):
            dict1[key] = update(dict1.get(key, {}), value)
        else:
            dict1[key] = dict2[key]
    return dict1

def procesar_definicion(instr, ts) :
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0, instr.ambito)      # inicializamos con 0 como valor por defecto
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    if(val!=None):
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
        elif(val == "asignacionarray"):
            procesar_indice_valor(instr,ts)
        elif(val == "declaracionarray"):
            procesar_definicion_array(instr,ts)
        elif(val == "conversion"):
            procesar_conversion(instr, ts)
        else:
            flag = ts.buscar(instr.id)
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val, instr.ambito)
            if(flag == True):
                ts.actualizar(simbolo)
            else:
                procesar_definicion(instr, ts)
                ts.actualizar(simbolo)
    else:
        print("Error: No se puede declarar esta variable por tipo de dato")

def procesar_unset(instr, ts):
    global erroresSemanticos
    if isinstance(instr.exp, ExpresionIdentificador):
        if ts.buscar(instr.exp.id):
            ts.borrar(instr.exp.id)
    else:
        Diccionario = {'Tipo':'Semantico','Error':str(instr.exp),'Descripcion':'Expresion a eliminar incompatible'}
        erroresSemanticos.agregar(Diccionario)
        shell.append(">> Error unset: "+str(instr.exp) +"\n Expresion a eliminar incompatible")

def procesar_conversion(instr, ts):
    val = resolver_expresion_aritmetica(instr.expNumerica.id, ts)
    tipoVal = ts.obtener(instr.expNumerica.id).valor
    newVal= ""
    if instr.expNumerica.tipo == "int":
        if type(tipoVal) == int:
            newVal = int(tipoVal)
        elif type(tipoVal) == float:
            newVal = int(tipoVal)
        elif type(tipoVal) == str:
            newVal = ord(tipoVal[0])
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, newVal, instr.ambito)
        if ts.buscar(instr.id):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif instr.expNumerica.tipo == "float":
        if type(tipoVal) == int:
            newVal = float(tipoVal)
        elif type(tipoVal) == float:
            newVal = float(tipoVal)
        elif type(tipoVal) == str:
            tipoVal = ord(tipoVal[0])
            newVal = float(tipoVal)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, newVal, instr.ambito)
        if ts.buscar(instr.id):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif instr.expNumerica.tipo == "char":
        if type(tipoVal) == int:
            newVal = chr(tipoVal)
        elif type(tipoVal) == float:
            tipoVal = int(tipoVal)
            newVal = chr(tipoVal)
        elif type(tipoVal) == str:
            newVal = tipoVal[0]
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, newVal, instr.ambito)
        if ts.buscar(instr.id):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif isinstance(tipoVal, dict):
        print("Arreglo")
    else:
        print(tipoVal,"--------",instr.expNumerica.id)
    #ts.agregar(simbolo)

def procesar_definicion_array(instr,ts):
    flag = ts.buscar(instr.id)
    if flag == True:
        diccionario = {}
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.ARRAY, diccionario, instr.ambito)
        ts.agregar(simbolo)
    else:
        diccionario = {}
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.ARRAY, diccionario, instr.ambito)
        ts.agregar(simbolo)

def procesar_asignacion_array(instr, ts):
    global erroresSemanticos
    indices = PILA.Pila()
    bkindices = PILA.Pila()
    indicesCopia = []
    flag = ts.buscar(instr.id)
    if flag == True:
        print("************ ",str(instr.id), " ***************")
        valorId = ts.obtener(instr.id).valor
        if isinstance(valorId,str):
            valorNew = resolver_expresion_aritmetica(instr.expNumerica, ts)
            ########## GET INDICES
            for expArray in instr.posicion:
                if isinstance(expArray, ExpresionArray):
                    print("Expresion Array Indice")
                    val = resolver_indice_valor(instr.expNumerica, ts)
                    if(val != None):
                        indicesCopia.append(val)
                    else: 
                        print("ERROR: Array o Struct no exist")
                        return
                elif isinstance(expArray, ExpresionNumerica):
                    val = resolver_expresion_aritmetica(expArray, ts)
                    if val == "cadena":
                        val = resolver_cadena(expArray, ts)
                        indicesCopia.append(val)
                    else:
                        indicesCopia.append(val)
            if valorNew == "cadena":
                valorNew = resolver_cadena(instr.expNumerica, ts)
            if indicesCopia[0] < len(valorId):
                arregloCadena = list(valorId)
                arregloCadena[indicesCopia[0]] = str(valorNew)
                cadena = "".join(arregloCadena)
                simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, cadena, instr.ambito)
                ts.actualizar(simbolo)
            else:
                arregloCadena = list(valorId)
                i = 0
                while True:
                    if(i == indicesCopia[0]):
                        arregloCadena.append(str(valorNew))
                        break
                    elif(i>=len(valorId)):
                        arregloCadena.append(" ")
                    i+=1
                cadena = "".join(arregloCadena)
                simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, cadena, instr.ambito)
                ts.actualizar(simbolo)
        else:
            valorNew = resolver_expresion_aritmetica(instr.expNumerica, ts)
            ########## GET INDICES
            for expArray in instr.posicion:
                if isinstance(expArray, ExpresionArray):
                    print("Expresion Array Indice")
                    val = resolver_indice_valor(instr.expNumerica, ts)
                    if(val != None):
                        indices.push(val)
                        bkindices.push(val)
                        indicesCopia.append(val)
                    else: 
                        print("ERROR: Array o Struct no exist")
                        return
                elif isinstance(expArray, ExpresionNumerica):
                    val = resolver_expresion_aritmetica(expArray, ts)
                    if val == "cadena":
                        val = resolver_cadena(expArray, ts)
                        indices.push(val)
                        bkindices.push(val)
                        indicesCopia.append(val)
                    else:
                        indices.push(val)
                        bkindices.push(val)
                        indicesCopia.append(val)
            ########## GET VALOR
            if (valorNew == "asignacionarray"):
                print("Expresion Array Valor")
                val = resolver_indice_valor(instr.expNumerica, ts)
                if(val != None):
                    valorNew = val
                else:
                    print("ERROR: Array o Struct no exist")
            elif (valorNew == "cadena"):
                valorNew = resolver_cadena(instr.expNumerica, ts)

            ##################### DICCIONARIO = VALOR
            valorAux = indices.pop()
            Diccionario = {valorAux: valorNew}
            while indices.estaVacia() == False:
                valorAux = indices.pop()
                auxDiccionario = {valorAux:Diccionario}
                Diccionario = auxDiccionario
            try:
                valorFinal = update(copy.deepcopy(valorId), Diccionario)
                simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.STRUCT, valorFinal, instr.ambito)
                ts.actualizar(simbolo)
            except:
                if type(valorId[indicesCopia[len(indicesCopia)-2]]) == str and type(indicesCopia[len(indicesCopia)-1]) == int:
                    if type(valorNew) == str:
                        cadena = valorId[indicesCopia[len(indicesCopia)-2]]
                        arregloCadena = list(cadena)
                        tamanio = len(arregloCadena) - int(indicesCopia[len(indicesCopia)-1])
                        if tamanio >= 0:
                            arregloCadena[indicesCopia[len(indicesCopia)-1]] = valorNew
                            cadena = "".join(arregloCadena)
                            bkindices.pop()
                            valorAux = bkindices.pop()
                            Diccionario = {valorAux: cadena}
                            while bkindices.estaVacia() == False:
                                valorAux = bkindices.pop()
                                auxDiccionario = {valorAux:Diccionario}
                                Diccionario = auxDiccionario
                            try:
                                #print("Nuevo valor: ",str(Diccionario))
                                #print("Valor de ts: ",str(valorId))
                                valorFinal = update(copy.deepcopy(valorId), Diccionario)
                                simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.STRUCT, valorFinal, instr.ambito)
                                ts.actualizar(simbolo)
                            except:
                                Diccionario = {'Tipo':'Semantico','Error':str(valorNew),'Descripcion':'Indice ocupado'}
                                erroresSemanticos.agregar(Diccionario)
                                shell.append(">> Error Indice ocupado: "+str(valorId) +"\n No se puede ingresar el valor: "+str(valorNew))
                        else:
                            Diccionario = {'Tipo':'Semantico','Error':str(valorNew),'Descripcion':'Indice ocupado'}
                            erroresSemanticos.agregar(Diccionario)
                            shell.append(">> Error Indice ocupado: "+str(valorId) +"\n No se puede ingresar el valor: "+str(valorNew))
                    else:
                        Diccionario = {'Tipo':'Semantico','Error':str(valorNew),'Descripcion':'Indice ocupado'}
                        erroresSemanticos.agregar(Diccionario)
                        shell.append(">> Error Indice ocupado: "+str(valorId) +"\n No se puede ingresar el valor: "+str(valorNew))
                else:
                    Diccionario = {'Tipo':'Semantico','Error':str(valorNew),'Descripcion':'Indice ocupado'}
                    erroresSemanticos.agregar(Diccionario)
                    shell.append(">> Error Indice ocupado: "+str(valorId) +"\n No se puede ingresar el valor: "+str(valorNew))
    else:
        procesar_definicion_array(instr, ts)
        procesar_asignacion_array(instr, ts)

def procesar_indice_valor(instr, ts):
    flag = ts.buscar(instr.id)
    if flag == True:
        val = resolver_indice_valor(instr.expNumerica, ts)
        try:
            valorFinal = int(val)
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, valorFinal, instr.ambito)
        except:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val, instr.ambito)
        ts.actualizar(simbolo)
    else:
        procesar_definicion(instr, ts)
        procesar_indice_valor(instr, ts)



def procesar_definicion_cadena(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, "", instr.ambito)
    ts.agregar(simbolo)

def procesar_asignacion_cadena(instr, ts):
    val = resolver_cadena(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val, instr.ambito)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_cadena(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_logica(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0, instr.ambito)
    ts.agregar(simbolo)

def procesar_asignacion_logica(instr, ts):
    val = resolver_expresion_binaria_logica(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val, instr.ambito)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_logica(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_logica_unitaria(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0, instr.ambito)
    ts.agregar(simbolo)

def procesar_asignacion_logica_unitaria(instr, ts):
    val = resolver_expresion_unitaria_logica(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val, instr.ambito)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_logica(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_bit(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, 0, instr.ambito)
    ts.agregar(simbolo)

def procesar_asignacion_bit(instr, ts):
    val = resolver_expresion_binaria_bit(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, val, instr.ambito)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_bit(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_bit_unitaria(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, 0, instr.ambito)
    ts.agregar(simbolo)

def procesar_asignacion_bit_unitaria(instr,ts):
    val = resolver_expresion_unitaria_bit(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BIT, val, instr.ambito)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_bit(instr, ts)
        ts.actualizar(simbolo)

def procesar_definicion_relacional(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0, instr.ambito)
    ts.agregar(simbolo)

def procesar_asignacion_relacional(instr, ts):
    val = resolver_expresion_binaria_relacional(instr.expNumerica, ts)
    flag = ts.buscar(instr.id)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, val, instr.ambito)
    if(flag == True):
        ts.actualizar(simbolo)
    else:
        procesar_definicion_relacional(instr,ts)
        ts.agregar(simbolo)

def procesar_goto(instr, instrucciones, ts):
    indice = 0
    flag = False
    while indice < len(instrucciones):
        instrGoto = instrucciones[indice]
        if isinstance(instrGoto, Etiqueta):
            if instrGoto.id == instr.id:
                procesar_instrucciones(instrucciones, indice, ts)
                flag = True
                break
        indice += 1
    if flag == False:
        print("Error: la etiequeta ",str(instr.id), " no existe")

def procesar_imprimir(expPrint, ts):
    global erroresSemanticos
    try:
        val = resolver_expresion_aritmetica(expPrint, ts)
        if val == "cadena":
            val = resolver_cadena(expPrint, ts)
            if val =="\\n":
                val = ""
        elif val == "asignacionarray":
            val = resolver_indice_valor(expPrint, ts)
            if val == None:
                Diccionario = {'Tipo':'Semantico','Error':str(expPrint.id),'Descripcion':'Los indices no existen'}
                erroresSemanticos.agregar(Diccionario)
                val = "Error Los indices no existen: " + str(expPrint.id)
        elif isinstance(val,dict):
            Diccionario = {'Tipo':'Semantico','Error':str(expPrint.id),'Descripcion':'No se puede imprimir un objeto de tipo arreglo o struct'}
            erroresSemanticos.agregar(Diccionario)
            val = "Error no se puede imprimir un arreglo o struct: "+ str(expPrint.id)
        shell.append(">>"+str(val))
    except:
        shell.append("Error:fatal en la impresion")

def procesar_if(expIf, ts):
    print("IF:", str(expIf))
    val = resolver_expresion_aritmetica(expIf.expLogica, ts)
    if(val!=None):
        if(val=="cadena"):
            val = resolver_cadena(expIf.expLogica, ts)
        elif(val=="logicabinaria"):
            resolver_expresion_binaria_logica(expIf.expLogica,ts)
        elif(val=="logicaunitaria"):
            val = resolver_expresion_unitaria_logica(expIf.expLogica,ts)
        elif(val == "bitbinaria"):
            val = resolver_expresion_binaria_bit(expIf.expLogica,ts)
        elif(val == "bitunitaria"):
            val = resolver_expresion_unitaria_bit(expIf.expLogica, ts)
        elif(val == "relacionalbinaria"):
            val = resolver_expresion_binaria_relacional(expIf.expLogica, ts)
        elif(val == "asignacionarray"):
            val = resolver_indice_valor(expIf.expLogica, ts)
        elif(val == "declaracionarray"):
            val = resolver_indice_valor(expIf.expLogica, ts)
        if val == 0:
             return 0
        elif val == 1:
            return 1
        else:
            return None
    else:
        print("Error: Condicional incorrecta ",str(val))


def resolver_indice_valor(expArray, ts):
    flag = ts.buscar(expArray.id)
    if flag == True:
        valorId = ts.obtener(expArray.id).valor
        cola = PILA.Pila()
        for expArreglo in expArray.indices:
            val = resolver_expresion_aritmetica(expArreglo, ts)
            if val == "cadena":
                val = resolver_cadena(expArreglo, ts)
                cola.agregar(val)
            elif val == "declaracionarray":
                val = resolver_indice_valor(expArreglo, ts)
                if val != None:
                    cola.agregar(val)
                else:
                    print("ERROR: Array o Struct no exist")
            elif val == "asignacionarray":
                val = resolver_indice_valor(expArreglo, ts)
                if val != None:
                    cola.agregar(val)
                else:
                    print("ERROR: Array o Struct no exist")
            else:
                cola.agregar(val)
        if type(valorId) == str:
            valorAux = valorId[cola.pop()]
            print("voy aqui y retornaer", valorAux)
            return valorAux
        else:
            try:
                valorAux = valorId.get(cola.pop())
            except:
                print("Error: estos indices no existen")
                return None
            try:
                while cola.estaVacia() == False:
                    valorAux = valorAux.get(cola.pop())
            except:
                print("Error: estos indices no existen")
                valorAux = None
            return valorAux
    else:
        print("Error: Este arreglo o struct no existe")
    

def resolver_cadena(expCad, ts) :
    #if isinstance(expCad, ExpresionConcatenar) :
    #    exp1 = resolver_cadena(expCad.exp1, ts)
    #    exp2 = resolver_cadena(expCad.exp2, ts)
    #    return exp1 + exp2
    if isinstance(expCad, ExpresionString):
        return expCad.val
    #elif isinstance(expCad, ExpresionCadenaNumerico) :
    #    return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')

def resolver_expresion_binaria_logica(expLog, ts) :
    global id
    global archivoDot
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

def graficar_expresion_unitaria_logica(expLog, ts):
    exp = resolver_expresion_aritmetica(expLog.exp, ts)
    graficar_expresion_unaria(expLog, ts, "!")
    if exp == 1:
        return 0
    elif exp == 0:
        return 1
    else:
        print("Error: LogicaUnitaria numero")

def resolver_expresion_binaria_bit(expBit, ts):
    global id
    global archivoDot
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
    global id
    global archivoDot
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
        if expNum.operador == OPERACION_ARITMETICA.MAS :
            return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : 
            return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR :
            return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO :
            return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.RESIDUO : 
            return exp1 % exp2
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
    elif isinstance(expNum, ExpresionArray):
        return "asignacionarray"
    elif isinstance(expNum, ExpresionDeclaracionArray):
        return "declaracionarray"
    elif isinstance(expNum, ExpresionConversion):
        return "conversion"

def graficar_expresion_aritmetica(expNum, ts) :
    global id
    global archivoDot
    if isinstance(expNum, ExpresionBinaria) :
        if expNum.operador == OPERACION_ARITMETICA.MAS :
            graficar_expresion_binaria(expNum, ts, "+")
        if expNum.operador == OPERACION_ARITMETICA.MENOS : 
            graficar_expresion_binaria(expNum, ts, "-")
        if expNum.operador == OPERACION_ARITMETICA.POR : 
            graficar_expresion_binaria(expNum, ts, "*")
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : 
            graficar_expresion_binaria(expNum, ts, "/")
        if expNum.operador == OPERACION_ARITMETICA.RESIDUO : 
            graficar_expresion_binaria(expNum, ts, "%")
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
    elif isinstance(expNum, ExpresionNotLogica):
        graficar_expresion_unaria(expNum,ts,"-")
    elif isinstance(expNum, ExpresionNotBit):
        graficar_expresion_unaria(expNum,ts,"~")
    elif isinstance(expNum, ExpresionNumero):
        archivoDot += expNum.graficar(id, expNum.val)
        id += 1
    elif isinstance(expNum, ExpresionIdentificador) :
        archivoDot += expNum.graficar(id,expNum.id)
        id += 1
    elif isinstance(expNum, ExpresionAbsoluto):
        graficar_expresion_unaria(expNum,ts,"abs")
    elif isinstance(expNum, ExpresionString) :
        archivoDot += expNum.graficar(id, expNum.val)
        id += 1
    elif isinstance(expNum, ExpresionBinariaLogica):
        if expNum.operador == OPERACION_LOGICA.AND :
            graficar_expresion_binaria(expNum,ts,"&&")
        elif expNum.operador == OPERACION_LOGICA.OR :
            graficar_expresion_binaria(expNum,ts,"||")
        elif expNum.operador == OPERACION_LOGICA.XOR :
            graficar_expresion_binaria(expNum,ts,"xor")
    elif isinstance(expNum, ExpresionBinariaBit):
        if expNum.operador == OPERACION_BIT.BAND :
            graficar_expresion_binaria(expNum, ts, "&")
        elif expNum.operador == OPERACION_BIT.BOR :
            graficar_expresion_binaria(expNum, ts, "|")
        elif expNum.operador == OPERACION_BIT.BXOR :
            graficar_expresion_binaria(expNum, ts, "^")
        elif expNum.operador == OPERACION_BIT.SHIFTI:
            graficar_expresion_binaria(expNum, ts, "<<")
        elif expNum.operador == OPERACION_BIT.SHIFTD:
            graficar_expresion_binaria(expNum, ts, ">>")
    elif isinstance(expNum, ExpresionBinariaRelacional):
        if expNum.operador == OPERACION_RELACIONAL.IGUAL :
            graficar_expresion_binaria(expNum, ts, "==")
        elif expNum.operador == OPERACION_RELACIONAL.DIFERENTE :
            graficar_expresion_binaria(expNum, ts, "!=")
        elif expNum.operador == OPERACION_RELACIONAL.MAYOR_QUE :
            graficar_expresion_binaria(expNum, ts, ">")
        elif expNum.operador == OPERACION_RELACIONAL.MENOR_QUE:
            graficar_expresion_binaria(expNum, ts, "<")
        elif expNum.operador == OPERACION_RELACIONAL.MAYORIGUAL_QUE:
            graficar_expresion_binaria(expNum, ts, ">=")
        elif expNum.operador == OPERACION_RELACIONAL.MENORIGUAL_QUE:
            graficar_expresion_binaria(expNum, ts, "<=")
    elif isinstance(expNum, ExpresionDeclaracionArray):
        archivoDot += expNum.graficar(id)
        id += 1
    elif isinstance(expNum, ExpresionConversion):
        archivoDot += expNum.graficar(id, expNum.id, expNum.tipo)
        id += 1
    elif isinstance(expNum, ExpresionArray):
        lista = []
        for expArray in expNum.indices:
            if isinstance(expArray, ExpresionNumero):
                lista.append(expArray.val)
            elif isinstance(expArray, ExpresionString):
                lista.append(expArray.val)
            elif isinstance(expArray, ExpresionIdentificador):
                lista.append(expArray.id)
        archivoDot += expNum.graficar(id, expNum.id, lista)
        id += 1

def getIndiceArray(expNum, ts):
    lista = []
    txt = ""
    for expArray in expNum:
        if isinstance(expArray, ExpresionNumero):
            lista.append(expArray.val)
        elif isinstance(expArray, ExpresionString):
            lista.append(expArray.val)
        elif isinstance(expArray, ExpresionIdentificador):
            lista.append(expArray.id)
    for x in range(len(lista)):
            txt = "["
            txt += str(lista[x])
            txt += "]"
    return txt

def procesar_instrucciones(instrucciones, indice, ts) :
    ## lista de instrucciones recolectadas
    while indice < len(instrucciones):
        instr = instrucciones[indice]
        if isinstance(instr, Imprimir) : 
            procesar_imprimir(instr.exp, ts)
        elif isinstance(instr, Asignacion):
            procesar_asignacion(instr, ts)
        elif isinstance(instr, AsignacionPosicionArray):
            procesar_asignacion_array(instr, ts)
        elif isinstance(instr, Etiqueta):
            flag = ts.buscar(instr.id)
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CONSTANTE, indice, "Main")
            if flag: ts.actualizar(simbolo)
            else: ts.agregar(simbolo)
            pass
        elif isinstance(instr, Goto):
            procesar_goto(instr, instrucciones, ts)
            break
        elif isinstance(instr, If) :
            condicion = procesar_if(instr, ts)
            if condicion == 1:
                procesar_goto(instr.id, instrucciones, ts)
                break
        elif isinstance(instr, Unset):
            procesar_unset(instr,ts)
        elif isinstance(instr, Exit):
            return
        elif isinstance(instr, Read):
            print('Read')
        else : print('Error: instrucción no válida')
        indice += 1

def graficar_procesar_instrucciones(instrucciones, indice, ts):
    global archivoDot
    global id
    global idP
    #for instr in instrucciones:
    while indice < len(instrucciones):
        instr = instrucciones[indice]
        if isinstance(instr, Imprimir) :
            graficar_expresion_aritmetica(instr.exp,ts)
            archivoDot+=instr.graficar(id, idP)
        elif isinstance(instr, Asignacion):
            graficar_expresion_aritmetica(instr.expNumerica, ts)
            archivoDot+=instr.graficar(id, idP, instr.id)
        elif isinstance(instr, AsignacionPosicionArray):
            graficar_expresion_aritmetica(instr.expNumerica, ts)
            txt = getIndiceArray(instr.posicion, ts)
            archivoDot += instr.graficar(id, idP, instr.id, txt)
        elif isinstance(instr, Etiqueta):
            archivoDot += instr.graficar(id, idP, instr.id)
        elif isinstance(instr, Goto):
            archivoDot += instr.graficar(id, idP, instr.id)
        elif isinstance(instr, If) :
            graficar_expresion_aritmetica(instr.expLogica, ts)
            archivoDot += instr.graficar(id, idP, instr.id.id)
            print(instr.id.id)
        elif isinstance(instr, Unset):
            graficar_expresion_aritmetica(instr.exp, ts)
            archivoDot+= instr.graficar(id, idP)
        elif isinstance(instr, Exit):
            archivoDot += instr.graficar(id, idP)
        else : print('Error: instrucción no válida')
        indice += 1
        id+=1
        idP+=1

def graficar_expresion_binaria(expG,ts, operador):
    global id
    global archivoDot
    exp1 = resolver_expresion_aritmetica(expG.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expG.exp2, ts)
    valor1=exp1
    valor2=exp2
    if isinstance(expG.exp1, ExpresionIdentificador):
        valor1=expG.exp1.id
    if isinstance(expG.exp2, ExpresionIdentificador):
        valor2=expG.exp2.id
    archivoDot += expG.graficar(id,valor1,valor2,operador)
    id += 3

def graficar_expresion_unaria(expGU, ts, operador):
    global id
    global archivoDot
    exp1 = resolver_expresion_aritmetica(expGU.exp, ts)
    valor = exp1
    if isinstance(expGU.exp, ExpresionIdentificador):
        valor = expGU.exp.id
    archivoDot += expGU.graficar(id, valor, operador)
    id += 1

def contadorPadre():
    global idP
    global archivoDot
    #archivoDot += "p0->" + "p"+str(idP)+";\n"
    contador = 0
    while contador < idP:
        archivoDot += "p"+str(contador)+"->p"+str(contador+1)+";\n"
        contador+=1
    
def astAsc():
    global archivoDot
    f = open("asc.dot", "w")
    f.write(archivoDot)
    f.close()

def crearTS(tablaSimbolos):
    tsg = ""
    tsg += "digraph H {\n"
    tsg += "aHtmlTable [\n"
    tsg += "shape=plaintext\n"
    tsg += "label=<\n"
    tsg += "<table border='1' cellborder='1'>\n"
    tsg += "<tr>\n"
    tsg += "<td>ID</td>\n"
    tsg += "<td>VALOR</td>\n"
    tsg += "<td>TIPO</td>\n"
    tsg += "<td>AMBITO</td>\n"
    tsg += "<td>DIMENSION</td>"
    tsg += "<td>REGISTRO/VARIABLE</td>"
    tsg += "</tr>\n"
    for x in tablaSimbolos.simbolos:
        tsg +="<tr>\n"
        tsg += "<td>"+ str(tablaSimbolos.simbolos[x].id) + "</td>\n"
        tsg += "<td>"+ str(tablaSimbolos.simbolos[x].valor) + "</td>\n"
        tsg += "<td>"+ str(tablaSimbolos.simbolos[x].tipo) + "</td>\n"
        tsg += "<td>"+ str(tablaSimbolos.simbolos[x].ambito) + "</td>\n"
        if type(tablaSimbolos.simbolos[x].valor) == dict:
            tsg += "<td>"+ str(len(tablaSimbolos.simbolos[x].valor)) + "</td>\n"
        else:
            tsg += "<td> </td>"
        tsg += "<td>"+ registroVar(tablaSimbolos.simbolos[x].id) + "</td>\n"
        tsg += "</tr>\n"
    tsg += "</table>\n"
    tsg += ">];\n"
    tsg += "}\n"
    f = open("tsg.dot","w")
    f.write(tsg)
    f.close()

def registroVar(id):
    if id == "$sp" : return "Puntero Pila"
    elif id == "$ra": return "Simulador direccion"
    elif id[1] == "t": return "temporal"
    elif id[1] == "a": return "parametro"
    elif id[1] == "v": return "valores devueltos por funciones"
    elif id[1] == "s": return "Pila"
    else: return "etiqueta"
    


def Main(input, consola):
    global archivoDot
    global idP
    archivoDot = ""
    idP=0
    global shell
    shell = consola
    instrucciones = g.parse(input)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones, 0, ts_global)
    archivoDot += "Digraph{\n p0[label=\"Main\"];\n"
    graficar_procesar_instrucciones(instrucciones, 0, ts_global)
    contadorPadre()
    archivoDot+="}"
    crearTS(ts_global)

erroresSemanticos = PILA.Pila()
shell = None
archivoDot = ""
id = 0
idP = 0

