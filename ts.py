from enum import Enum

class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2
    BOOL = 3
    BIT = 4

class Simbolo():
    #Clase que representa un simbolo en la TS
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaDeSimbolos():
    #Tabla de simbolos

    def __init__(self, simbolos = {}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id):
        if not id in self.simbolos:
            print('Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def actualizar(self, simbolo):
        if not simbolo.id in self.simbolos :
            print('Error: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo
            
    def buscar(self, id):
        if not id in self.simbolos:
            print('Error: variable ', id, ' no definida.')
            return False
        return True