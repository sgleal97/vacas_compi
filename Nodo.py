txt = ""
cont = 0

def incrementarContador():
    global cont
    cont += 1
    return "%d" %cont

class Nodo():
    pass

class init(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+name)

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class lista_instrucciones(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class instrucciones_instruccion(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class instruccion(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class asignacion(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class asignacion_conversion(Nodo):
    def __init__(self, name):
        self.name = name

    #def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class exp_numerica_binaria(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class exp_numerica_unaria(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class exp_numerica_abs(nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class exp_numerica_valores(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class exp_id(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class exp_cadena(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(ident):

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class ifIns(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()
        return id
    
class condicion(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()
        return id

class etiqueta(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()
        return id

class goto(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()
        return id
