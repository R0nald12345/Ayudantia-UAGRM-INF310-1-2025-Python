from ArbolMVias import ArbolMVias

if __name__ == "__main__":
    arbol = ArbolMVias()
    datos = [103, 120, 70, 180, 155, 110, 105]
    for x in datos:
        arbol.insertar(x)

    print("Recorrido inorden:")
    arbol.inorden()

    print("\nRecorrido por niveles:")
    arbol.niveles()

    print("Cantidad de Numeros Impares: " , arbol.contar_impares())

    print("Cantidad de Nodos: " , arbol.contar_nodos())
