from enum import Enum

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

class ExpresionBinaria(ExpresionNumerica):
    #Expresion binaria numerica
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionBinariaLogica(ExpresionNumerica):
    #Expresion binaria logica
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNegativo(ExpresionNumerica) :
    #Asigna la expresion para convertirla en negativa
    def __init__(self, exp) :
        self.exp = exp

class ExpresionNumero(ExpresionNumerica) :
    #Float o int
    def __init__(self, val = 0) :
        self.val = val

class ExpresionString(ExpresionNumerica):
    #Cadena
    def __init__(self, val = ""):
        self.val = val

class ExpresionAbsoluto(ExpresionNumerica):
    #Valor Absoluto
    def __init__(self, exp):
        self.exp = exp

class ExpresionIdentificador(ExpresionNumerica) :
    #ID
    def __init__(self, id = "") :
        self.id = id

class ExpresionNotLogica(ExpresionNumerica):
    #Not Logica
    def __init__(self, exp) :
        self.exp = exp

class ExpresionBinariaBit(ExpresionNumerica):
    #Expresion binaria bit a bit
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNotBit(ExpresionNumerica):
    #Not bit a bit
    def __init__(self,exp):
        self.exp = exp

class ExpresionBinariaRelacional(ExpresionNumerica):
    #Expresion binaria relacional
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

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


