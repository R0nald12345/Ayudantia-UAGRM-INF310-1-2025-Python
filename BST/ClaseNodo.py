class Nodo:
    def __init__(self, dato):
        self.__dato__ = dato
        self.__hijoIzquierdo__ = None
        self.__hijoDerecho__ = None

    def getDato(self):
        return self.__dato__

    def setDato(self, dato):
        self.__dato__ = dato

    def getHijoIzquierdo(self):
        return self.__hijoIzquierdo__

    def setHijoIzquierdo(self, hijoIzquierdo):
        self.__hijoIzquierdo__ = hijoIzquierdo

    def getHijoDerecho(self):
        return self.__hijoDerecho__

    def setHijoDerecho(self, hijoDerecho):
        self.__hijoDerecho__ = hijoDerecho