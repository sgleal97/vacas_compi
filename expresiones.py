from enum import Enum

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4

class OPERACION_LOGICA(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4

class ExpresionNumerica:
    '''Clase abstracta de expresion numerica'''

class ExpresionBinaria(ExpresionNumerica):
    #Expresion binaria
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

class ExpresionIdentificador(ExpresionNumerica) :
    #ID
    def __init__(self, id = "") :
        self.id = id

class ExpresionCadena:
    '''Clase abstracta de una cadena'''

class ExpresionConcatenar(ExpresionCadena) :
    #Concatenacion de 2 cadenas
    def __init__(self, exp1, exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionDobleComilla(ExpresionCadena) :
    #Cadena
    def __init__(self, val) :
        self.val = val

