from enum import Enum
import pila as PILA

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    RESIDUO = 5

class OPERACION_RELACIONAL(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MENORIGUAL_QUE = 5
    MAYORIGUAL_QUE = 6

class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3
    XOR = 4

class OPERACION_BIT(Enum):
    BAND = 1
    BOR = 2
    BNOT = 3
    BXOR = 4
    SHIFTI = 5
    SHIFTD = 6

class ExpresionNumerica:
    '''Clase abstracta de expresion numerica'''

class ExpresionConversion(ExpresionNumerica):
    #Conersion de variables
    def __init__(self, tipo, id = "") :
        self.tipo = tipo
        self.id = id

    def graficar(self, id, exp, tipo):
        nodo1 = exp
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(tipo)+"("+str(nodo1)+")\"];\n"
        return grafo

class ExpresionAsignacion(ExpresionNumerica):
    def graficar(self, id):
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\"Asignacion\"];\n"
        grafo += "nodo"+str(id)+"->nodo"+str(id+1)+";\n"
        return grafo

class ExpresionBinaria(ExpresionNumerica):
    #Expresion binaria numerica
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

    def graficar(self, id, exp1, exp2, operador):
        nodo1=exp1
        nodo2=exp2
        nodo3=operador
        auxId = id
        grafo = ""
        auxId += 1
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        grafo += "nodo"+str(id+2)+"[label=\""+str(nodo2)+"\"];\n"
        grafo += "nodo"+str(id+3)+"[label=\""+str(nodo3)+"\"];\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+1)+";\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+2)+";\n"
        return grafo

    def valorId(self, id):
        return 3

class ExpresionBinariaLogica(ExpresionNumerica):
    #Expresion binaria logica
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

    def graficar(self, id, exp1, exp2, operador):
        nodo1=exp1
        nodo2=exp2
        nodo3=operador
        auxId = id
        grafo = ""
        auxId += 1
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        grafo += "nodo"+str(id+2)+"[label=\""+str(nodo2)+"\"];\n"
        grafo += "nodo"+str(id+3)+"[label=\""+str(nodo3)+"\"];\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+1)+";\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+2)+";\n"
        return grafo

class ExpresionNegativo(ExpresionNumerica) :
    #Asigna la expresion para convertirla en negativa
    def __init__(self, exp) :
        self.exp = exp

    def graficar(self, id, exp, operador):
        nodo1 = exp
        nodo2 = operador
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\"-"+str(nodo1)+"\"];\n"
        return grafo

class ExpresionNumero(ExpresionNumerica) :
    #Float o int
    def __init__(self, val = 0) :
        self.val = val

    def graficar(self, id, exp):
        nodo1 = exp
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        return grafo

class ExpresionString(ExpresionNumerica):
    #Cadena
    def __init__(self, val = ""):
        self.val = val
    
    def graficar(self, id, exp):
        nodo1 = exp
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        return grafo

class ExpresionAbsoluto(ExpresionNumerica):
    #Valor Absoluto
    def __init__(self, exp):
        self.exp = exp

    def graficar(self, id, exp, operador):
        nodo1 = exp
        nodo2 = operador
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\"abs("+str(nodo1)+")\"];\n"
        return grafo

class ExpresionIdentificador(ExpresionNumerica) :
    #ID
    def __init__(self, id = "") :
        self.id = id

    def graficar(self, id, exp):
        nodo1 = exp
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        return grafo

class ExpresionNotLogica(ExpresionNumerica):
    #Not Logica
    def __init__(self, exp) :
        self.exp = exp

    def graficar(self, id, exp, operador):
        nodo1 = exp
        nodo2 = operador
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\"!"+str(nodo1)+"\"];\n"
        return grafo

class ExpresionBinariaBit(ExpresionNumerica):
    #Expresion binaria bit a bit
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

    def graficar(self, id, exp1, exp2, operador):
        nodo1=exp1
        nodo2=exp2
        nodo3=operador
        auxId = id
        grafo = ""
        auxId += 1
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        grafo += "nodo"+str(id+2)+"[label=\""+str(nodo2)+"\"];\n"
        grafo += "nodo"+str(id+3)+"[label=\""+str(nodo3)+"\"];\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+1)+";\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+2)+";\n"
        return grafo

class ExpresionNotBit(ExpresionNumerica):
    #Not bit a bit
    def __init__(self,exp):
        self.exp = exp

    def graficar(self, id, exp, operador):
        nodo1 = exp
        nodo2 = operador
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\"~"+str(nodo1)+"\"];\n"
        return grafo

class ExpresionBinariaRelacional(ExpresionNumerica):
    #Expresion binaria relacional
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

    def graficar(self, id, exp1, exp2, operador):
        nodo1=exp1
        nodo2=exp2
        nodo3=operador
        auxId = id
        grafo = ""
        auxId += 1
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        grafo += "nodo"+str(id+2)+"[label=\""+str(nodo2)+"\"];\n"
        grafo += "nodo"+str(id+3)+"[label=\""+str(nodo3)+"\"];\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+1)+";\n"
        grafo += "nodo"+str(id+3)+"->nodo"+str(id+2)+";\n"
        return grafo

class ExpresionArray(ExpresionNumerica):

    def __init__(self, id, indices):
        self.id = id
        self.indices = indices

    def graficar(self, id, exp, indices):
        auxId = id
        nodo1 = exp
        nodo2 = indices
        grafo = ""
        valInd = ""
        for x in range(len(nodo2)):
            print(nodo2[x])
            valInd += "["
            valInd += str(nodo2[x])
            valInd += "]"
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+str(valInd)+"\"];\n"
        return grafo



class ExpresionDeclaracionArray(ExpresionNumerica):

    def __init__(self, id = ""):
        self.id = id

    def graficar(self, id):
        nodo1 = "array()"
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        return grafo

class ExpresionApuntador(ExpresionNumerica):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionCadena:
    '''Clase abstracta de una cadena'''

class ExpresionConcatenar(ExpresionCadena) :
    #Concatenacion de 2 cadenas
    def __init__(self, exp1, exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionDobleComilla(ExpresionCadena) :
    #Imprimir
    def __init__(self, val) :
        self.val = val


