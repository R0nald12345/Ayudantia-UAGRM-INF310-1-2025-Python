class NodoM:
    M = 3  # Grado del árbol

    def __init__(self, x=None):
        self.hijo = [None] * NodoM.M
        self.data = [0] * (NodoM.M - 1)
        self.usada = [False] * (NodoM.M - 1)
        self.cantUsadas = 0
        if x is not None:
            self.setData(1, x)

    def getHijo(self, i):
        if 1 <= i <= len(self.hijo):
            return self.hijo[i - 1]
        return None

    def setHijo(self, i, p):
        if 1 <= i <= len(self.hijo):
            self.hijo[i - 1] = p

    def getData(self, i):
        if 1 <= i <= len(self.data):
            return self.data[i - 1]
        return 0

    def setData(self, i, x):
        if 1 <= i <= len(self.data):
            self.data[i - 1] = x
            if self.isVacia(i):
                self.cantUsadas += 1
            self.usada[i - 1] = True

    def existe(self, x):
        for i in range(len(self.data)):
            if self.usada[i] and self.data[i] == x:
                return True
        return False

    def insData(self, i, x):
        if 1 <= i <= len(self.data):
            self.expand(i - 1)
            self.setData(i, x)

    def insDataInOrden(self, x):
        i = 0
        n = self.cantDatasUsadas() - 1
        while i <= n and x > self.data[i]:
            i += 1
        if i <= n and x == self.data[i]:
            return
        if self.isLleno():
            print(f"NodoM.insDataInOrden: {x} no se puede insertar porque el nodo está lleno.")
            return
        self.insData(i + 1, x)

    def setVacia(self, i):
        if 1 <= i <= len(self.usada):
            if self.isUsada(i):
                self.cantUsadas -= 1
            self.usada[i - 1] = False

    def isVacia(self, i):
        if 1 <= i <= len(self.usada):
            return not self.usada[i - 1]
        return False

    def isUsada(self, i):
        if 1 <= i <= len(self.usada):
            return self.usada[i - 1]
        return False

    def cantHijos(self):
        return sum(1 for h in self.hijo if h is not None)

    def cantDatasUsadas(self):
        return self.cantUsadas

    def cantDatasVacias(self):
        return len(self.data) - self.cantUsadas

    def isLleno(self):
        return self.cantDatasVacias() == 0

    def __str__(self):
        S = "["
        pipe = ""
        for i in range(len(self.data)):
            S += pipe + (str(self.data[i]) if self.usada[i] else " ")
            pipe = "|"
        S += "]"
        return S

    def copyData(self, i, k):
        self.data[k] = self.data[i]
        self.usada[k] = self.usada[i]

    def expand(self, j):
        for i in range(len(self.data) - 1, j, -1):
            self.copyData(i - 1, i)
        self.updateCantUsadas()

    def updateCantUsadas(self):
        self.cantUsadas = sum(1 for used in self.usada if used)