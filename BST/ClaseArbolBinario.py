
from ClaseNodo import Nodo

class ArbolBinario:

    # Constructor de la clase ArbolBinario
    def __init__(self):
        self.__raiz__ = None

    #insertar Nodo (Procedimiento)
    def insertarNodo(self, x ):
        self.__raiz__ = self.__insertarNodoRecursivo(self.__raiz__, x)

    def __insertarNodoRecursivo(self, nodoRaiz,x):
        #Caso base
        if(nodoRaiz == None):
            return Nodo(x)
        else:
            if( x < nodoRaiz.getDato()): #en el caso que es Menor que el nodo raiz
                nodoRaiz.setHijoIzquierdo(self.__insertarNodoRecursivo(nodoRaiz.getHijoIzquierdo(), x))
            else: #en el caso que es Mayor que el nodo raiz
                nodoRaiz.setHijoDerecho(self.__insertarNodoRecursivo(nodoRaiz.getHijoDerecho(), x))

        #Retorna el nodo raiz
        return nodoRaiz
    
    def recorridoInOrden(self):
        self.__recorridoInOrdenRecursivo(self.__raiz__)
    
    def __recorridoInOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            self.__recorridoInOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            print(nodoRaiz.getDato(), end=" ")
            self.__recorridoInOrdenRecursivo(nodoRaiz.getHijoDerecho())

     
    def recorridoPreOrden(self):
        self.__recorridoPreOrdenRecursivo(self.__raiz__)
    
    def __recorridoPreOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            print(nodoRaiz.getDato(), end=" ")
            self.__recorridoPreOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            self.__recorridoPreOrdenRecursivo(nodoRaiz.getHijoDerecho())

     
    def recorridoPostOrden(self):
        self.__recorridoPostOrdenRecursivo(self.__raiz__)
    
    def __recorridoPostOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            self.__recorridoPostOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            self.__recorridoPostOrdenRecursivo(nodoRaiz.getHijoDerecho())
            print(nodoRaiz.getDato(), end=" ")
    

    def isVacio(self):
        return self.__raiz__ == None

    def isHoja(self, nodoRaiz):
        return nodoRaiz.getHijoIzquierdo() == None and nodoRaiz.getHijoDerecho() == None

    def contarNodos(self):
        return self.__contarNodosRecursivo(self.__raiz__)
    
    def __contarNodosRecursivo(self, nodoRaizAux):
        if(nodoRaizAux == None): #Caso Base ARbol Vacio
            return 0
        else:
            if(self.isHoja(nodoRaizAux)):#Caso base ARbol tiene 1 solo Nodo
                return 1
            else: # Caso General
                i = self.__contarNodosRecursivo(nodoRaizAux.getHijoIzquierdo()) #2
                d = self.__contarNodosRecursivo(nodoRaizAux.getHijoDerecho())  #1
                return d + i + 1


    def recorridoPorNivel(self):
        if self.__raiz__ is None:
            print("El árbol está vacío.")
            return

        cola = deque()  # Creamos una cola
        cola.append(self.__raiz__)  # Agregamos la raíz a la cola

        while cola:
            nodoActual = cola.popleft()  # Sacamos el nodo al frente de la cola
            
            if nodoActual is not None:
                print(nodoActual.getDato(), end=" ")  # Procesamos el nodo actual
                
                # Agregamos los hijos del nodo actual a la cola
                if nodoActual.getHijoIzquierdo() is not None:
                    cola.append(nodoActual.getHijoIzquierdo())
                if nodoActual.getHijoDerecho() is not None:
                    cola.append(nodoActual.getHijoDerecho())
        print()  # Salto de línea al final del recorrido

    def eliminar(self, x):
        self.__raiz__ = self.__eliminarRecursivo(self.__raiz__, x)

    
    def __eliminarRecursivo(self, nodoRaiz, x):
        #Caso Base
        if nodoRaiz is None:
            return None
        
        #Caso base
        if(x == nodoRaiz.getDato()):
            return self.eliminarNodo(nodoRaiz)
        
        #Caso general
        if x < nodoRaiz.getDato():
            nodoRaiz.setHijoIzquierdo(self.__eliminarRecursivo(nodoRaiz.getHijoIzquierdo(), x))
        else:
            nodoRaiz.setHijoDerecho(self.__eliminarRecursivo(nodoRaiz.getHijoDerecho(), x))
        
        return nodoRaiz

    def eliminarNodo(self, nodo):
        #1)Si mi nodo es hoja
        if self.isHoja(nodo):
            return None
        
        #2) Si mi nodo incompleto tiene solo 1 hijo
        if (nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is not None):
            return nodo.getHijoDerecho()
        
        if(nodo.getHijoIzquierdo() is not None and nodo.getHijoDerecho() is None):
            return nodo.getHijoIzquierdo()
        
        #3) Si mi arbol tiene varios Nodos
        nodoVerdeDato = self.__buscarSiguienteSucesor(nodo.getHijoDerecho()) #Doy un paso a la Derecha
        #ahora intercambio
        nodo.setDato(nodoVerdeDato)
        nodo.setHijoDerecho(self.__eliminarRecursivo(nodo.getHijoDerecho(), nodoVerdeDato))
        return nodo

    def __buscarSiguienteSucesor(self, nodoDerecho):
        while(nodoDerecho.getHijoIzquierdo() is not None):
            nodoDerecho = nodoDerecho.getHijoIzquierdo()
        return nodoDerecho.getDato()
    

if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertarNodo(100)
    arbol.insertarNodo(80)
    arbol.insertarNodo(120)
    arbol.insertarNodo(70)


    arbol.recorridoInOrden()  # Salida: 70 80 100 120
    arbol.eliminar(100)
    print()
    print('Nuevo Arbol')
    arbol.recorridoInOrden()  # Salida: 70 80 120
    #print()
    #arbol.recorridoPreOrden() 
    #print()
    #arbol.recorridoPostOrden() 
   
    #print()
    #print("Cantidad de nodos:", arbol.contarNodos()) 