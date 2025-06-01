class GrafoNoDirigido:
    def __init__(self):
        self.lista_de_adyacencia = []
        self.cant_aristas = 0

    def insertar_vertice(self):
        self.lista_de_adyacencia.append([])

    def cantidad_aristas(self):
        return self.cant_aristas

    def cantidad_de_vertice(self):
        return len(self.lista_de_adyacencia)

    def validar_vertice(self, pos_vertice):
        if pos_vertice < 0 or pos_vertice >= self.cantidad_de_vertice():
            raise Exception(f"Error al validar el vértice: {pos_vertice}")

    def insertar_arista(self, origen, destino):
        self.validar_vertice(origen)
        self.validar_vertice(destino)
        if self.verificar_adyacencia(origen, destino):
            raise Exception(f"Ya existe la adyacencia entre los vértices: {origen} y {destino}")

        self.cant_aristas += 1


        #-------------------------------------
        # self.lista_de_adyacencia[origen].append(destino)

        # if origen != destino:  # Evitar duplicados en caso de bucle
        #     self.lista_de_adyacencia[destino].append(origen)

        #-------------------------------------

        self.lista_de_adyacencia[origen].append(destino)

    def verificar_adyacencia(self, origen, destino):
        return destino in self.lista_de_adyacencia[origen]

    def mostrar_grafo_no_dirigido(self):
        for i, adyacentes in enumerate(self.lista_de_adyacencia):
            adyacencia_str = ",".join(map(str, adyacentes))
            print(f"[{i}] -> {adyacencia_str}")


def main():
    try:
        grafo = GrafoNoDirigido()

        # Insertar 4 vértices (0 a 3)
        for _ in range(4):
            grafo.insertar_vertice()

        # Insertar algunas aristas
        # grafo.insertar_arista(0, 1)
        # grafo.insertar_arista(0, 2)
        # grafo.insertar_arista(1, 0)  # Ya existe relación
        # grafo.insertar_arista(1, 2)
        # grafo.insertar_arista(1, 3)
        # grafo.insertar_arista(2, 0)  # Ya existe relación
        # grafo.insertar_arista(2, 1)  # Ya existe relación
        # grafo.insertar_arista(3, 1)  # Ya existe relación

        grafo.insertar_arista(0, 1)
        grafo.insertar_arista(1, 3)
        grafo.insertar_arista(2, 0)
        grafo.insertar_arista(2, 1)

        # Mostrar resultados
        print("Cantidad de vértices:", grafo.cantidad_de_vertice())
        print("Cantidad de aristas:", grafo.cantidad_aristas())
        print("Representación del grafo:")
        grafo.mostrar_grafo_no_dirigido()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
