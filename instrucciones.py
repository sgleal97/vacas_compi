class Instruccion:
    '''Clase abstracta de instruccion'''

class Definicion(Instruccion) :
    '''Instruccion definicion, parametro ID'''

    def __init__(self, id, ambito) :
        self.id = id

class Asignacion(Instruccion):
    '''Instruccion asignacion, parametro ID y valor'''

    def __init__(self, id, expNumerica, ambito):#Se agrego ambito
        self.id = id
        self.expNumerica = expNumerica
        self.ambito = ambito#Se agrego ambito

    def graficar(self, id, idP, var):
        nodo1 = var
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+"\"];\n"
        grafo += "p"+str(idP+1)+"[label=\"Asignacion\"];\n"
        grafo += "p"+str(idP+1)+"->nodo"+str(id+1)+";\n"
        grafo += "nodo"+str(id+1)+"->nodo"+str(id)+";\n"
        auxId += 1
        return grafo

class AsignacionPosicionArray(Instruccion):

    def __init__(self, id, posicion, expNumerica, ambito):
        self.id = id
        self.posicion = posicion
        self.expNumerica = expNumerica
        self.ambito = ambito

    def graficar(self, id, idP, var, posicion):
        nodo1 = var
        auxId = id
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\""+str(nodo1)+str(posicion)+"\"];\n"
        grafo += "p"+str(idP+1)+"[label=\"ArrayAsignacion\"];\n"
        grafo += "p"+str(idP+1)+"->nodo"+str(id+1)+";\n"
        grafo += "nodo"+str(id+1)+"->nodo"+str(id)+";\n"
        auxId += 1
        return grafo

class Etiqueta(Instruccion):

    def __init__(self, id):
        self.id = id
    
    def graficar(self, id, idP, var):
        nodo1 = var
        grafo = ""
        grafo += "p"+str(idP+1)+"[label=\"Etiqueta("+str(nodo1)+")\"];\n"
        return grafo

class Goto(Instruccion):
    
    def __init__(self, id):
        self.id = id

    def graficar(self, id, idP, var):
        nodo1 = var
        grafo = ""
        grafo += "p"+str(idP+1)+"[label=\"goto "+str(nodo1)+"\"];\n"
        return grafo

class AsignacionCadena(Instruccion):
    '''Instruccion asignacion, parametro ID y valor'''

    def __init__(self, id, expCadena, ambito):
        self.id = id
        self.expCadena = expCadena

class Imprimir(Instruccion):
    '''Imprime un registro'''

    def __init__(self, exp):
        self.exp = exp

    def graficar(self, id, idP):
        grafo = ""
        grafo += "p"+str(idP+1)+"[label=\"Print\"];\n"
        grafo += "p"+str(idP+1)+"->nodo"+str(id)+";\n"
        return grafo

class Unset(Instruccion):
    '''Destruye las variables'''

    def __init__(self, exp):
        self.exp = exp

    def graficar(self, id, idP):
        grafo = ""
        grafo += "p"+str(idP+1)+"[label=\"Unset \"];\n"
        grafo += "p"+str(idP+1)+"->nodo"+str(id)+";\n"
        return grafo

class If(Instruccion):
    ''' Instruccion If, codicion; lisaInstruccions'''

    def __init__(self, expLogica, id):
        self.expLogica = expLogica
        self.id = id

    def graficar(self, id, idP, var):
        nodo1 = var
        grafo = ""
        grafo += "nodo"+str(id+1)+"[label=\"goto "+str(nodo1)+"\"];\n"
        grafo += "p"+str(idP+1)+"[label=\"if\"];\n"
        grafo += "p"+str(idP+1)+"->nodo"+str(id)+";\n"
        grafo += "p"+str(idP+1)+"->nodo"+str(id+1)+";\n"
        return grafo

class Exit(Instruccion):

    def __init__(self, id=""):
        self.id = id

    def graficar(self, id, idP):
        grafo = ""
        grafo += "p"+str(idP+1)+"[label=\"exit\"];\n"
        return grafo