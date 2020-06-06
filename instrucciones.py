class Instruccion:
    '''Clase abstracta de instruccion'''

class Definicion(Instruccion) :
    '''Instruccion definicion, parametro ID'''

    def __init__(self, id) :
        self.id = id

class Asignacion(Instruccion):
    '''Instruccion asignacion, parametro ID y valor'''

    def __init__(self, id, expNumerica):
        self.id = id
        self.expNumerica = expNumerica

