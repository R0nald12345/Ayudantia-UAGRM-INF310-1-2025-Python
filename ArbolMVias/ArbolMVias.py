from NodoMVias import NodoM
from collections import deque

class ArbolMVias:
    def __init__(self):
        self.raiz = None

    def insertar(self, x):
        if self.raiz is None:
            self.raiz = NodoM(x)
        else:
            p = self.raiz
            ant = None
            i = 0
            while p is not None:
                if not p.isLleno():
                    p.insDataInOrden(x)
                    return
                i = self.hijoDesc(p, x)
                if i == -1:
                    return  # x ya está en el árbol
                ant = p
                p = p.getHijo(i)
            nuevo = NodoM(x)
            ant.setHijo(i, nuevo)

    def hijoDesc(self, nodo, x):
        i = 1
        while i <= len(nodo.data):
            if nodo.isUsada(i):
                if x < nodo.getData(i):
                    return i
                if x == nodo.getData(i):
                    return -1
            i += 1
        return len(nodo.data) + 1

    def inorden(self):
        print("Inorden:", end=" ")
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo is not None:
            z = nodo.cantDatasUsadas()
            for i in range(1, z + 1):
                self._inorden(nodo.getHijo(i))
                print(nodo.getData(i), end=" ")
            self._inorden(nodo.getHijo(z + 1))

    def niveles(self):
        if self.raiz is None:
            print("Árbol vacío")
            return
        cola = deque()
        cola.append((self.raiz, 0))  # <-- Cambiado a 0 para el nivel raíz
        nivel_actual = -1
        print("Por niveles:")
        while cola:
            nodo, nivel = cola.popleft()
            if nivel != nivel_actual:
                print(f"\nNivel {nivel}: ", end="")
                nivel_actual = nivel
            print(nodo, end=" ")
            for i in range(1, len(nodo.hijo) + 1):
                hijo = nodo.getHijo(i)
                if hijo is not None:
                    cola.append((hijo, nivel + 1))
        print()


    # 2 Casos bases 1 General
    def contar_impares(self):
        return self._contar_imparesRecursivo(self.raiz)

    def _contar_imparesRecursivo(self, raizAux):
        #caso base 
        if raizAux is None:
            return 0
        
        contador = 0
        # Recorremos los datos del nodo Padre
        for i in range(1, raizAux.cantDatasUsadas() + 1):
            if raizAux.getData(i) % 2 != 0:
                contador += 1

        # caso recursivo (Caso General)
        #Recorro todos los hijos del nodo padre
        for i in range(1, len(raizAux.hijo) + 1):
            contador+= self._contar_imparesRecursivo(raizAux.getHijo(i))
        
        return contador
    
    
    def contar_nodos(self):
        return self._contar_nodosRecursivo(self.raiz)

    def _contar_nodosRecursivo(self, raizAux):
        #caso base 
        if raizAux is None:
            return 0
        
        contador = 0
       
        # caso recursivo (Caso General)
        #Recorro todos los hijos del nodo padre
        for i in range(1, len(raizAux.hijo) + 1):
            contador+= self._contar_nodosRecursivo(raizAux.getHijo(i))
        
        return contador+1
            
