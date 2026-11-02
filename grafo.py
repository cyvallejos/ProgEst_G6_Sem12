def agregar_vertice(grafo, vertice):
    #Agrega un vértice al grafo si no existe.
    if vertice not in grafo:
        grafo[vertice] = []
    return True


def agregar_arista(grafo, origen, destino):
    #Agrega una arista no dirigida entre dos vértices.
    for vertice in (origen, destino):
        agregar_vertice(grafo, vertice)

    if origen == destino:
        return False

    if destino not in grafo[origen]:
        grafo[origen].append(destino)
        if origen != destino:
            if destino not in grafo or origen not in grafo:
                return True
            if origen not in grafo[destino]:
                grafo[destino].append(origen)
        return True

    return False


def consultar_vecinos(grafo, vertice):
    #Devuelve la lista de vecinos de un vértice.
    if vertice not in grafo:
        return []
    return list(grafo[vertice])


def existe_arista(grafo, origen, destino):
    #Comprueba si existe una conexión directa entre dos vértices.
    if origen not in grafo:
        return False
    return destino in grafo[origen]


def mostrar_grafo(grafo):
    #Muestra cada vértice junto con sus vecinos.
    for vertice in grafo:
        print(f"{vertice} -> {consultar_vecinos(grafo, vertice)}")


def matriz_adyacencia(vertices, conexiones):
    #Construye la matriz de adyacencia para un grafo no dirigido.
    n = len(vertices)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    indice = {vertice: i for i, vertice in enumerate(vertices)}

    for origen, destino in conexiones:
        matriz[indice[origen]][indice[destino]] = 1
        matriz[indice[destino]][indice[origen]] = 1

    return matriz


def mostrar_matriz(vertices, matriz):
    #Muestra la matriz en formato legible.
    print(" ".join([" "] + vertices))
    for i, fila in enumerate(matriz):
        print(vertices[i], *fila)


def eliminar_arista(grafo, origen, destino):
    #Elimina una arista entre dos vértices.
    if origen not in grafo or destino not in grafo:
        return False

    if destino in grafo[origen]:
        grafo[origen].remove(destino)
    if origen in grafo[destino]:
        grafo[destino].remove(origen)
    return True


def eliminar_vertice(grafo, vertice):
    #Elimina un vértice y todas las referencias a él.
    if vertice not in grafo:
        return False

    for otro in list(grafo):
        if otro == vertice:
            continue
        if vertice in grafo[otro]:
            grafo[otro].remove(vertice)

    del grafo[vertice]
    return True


def agregar_arista_ponderada(grafo, origen, destino, costo):
    #Agrega una arista ponderada usando un diccionario anidado.
    for vertice in (origen, destino):
        if vertice not in grafo:
            grafo[vertice] = {}

    if origen not in grafo[destino]:
        grafo[destino][origen] = costo
    if destino not in grafo[origen]:
        grafo[origen][destino] = costo

    return True


def costo_directo(grafo, origen, destino):
    #Devuelve el costo de una conexión directa o None si no existe.
    if origen not in grafo:
        return None

    if isinstance(grafo[origen], dict):
        return grafo[origen].get(destino)

    if destino in grafo[origen]:
        return 1
    return None


def ejemplo_grafo_no_dirigido():
    grafo = {
        "Managua": ["León", "Granada", "Masaya"],
        "León": ["Managua"],
        "Granada": ["Managua", "Masaya"],
        "Masaya": ["Managua", "Granada"],
    }
    print("Ejemplo 1. Crear y mostrar un grafo no dirigido")
    mostrar_grafo(grafo)
    print("\nVecinos de Managua:", consultar_vecinos(grafo, "Managua"))
    print("¿Conexión León-Granada?:", existe_arista(grafo, "León", "Granada"))


def ejemplo_matriz_adyacencia():
    vertices = ["A", "B", "C", "D"]
    conexiones = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D")]
    matriz = matriz_adyacencia(vertices, conexiones)
    print("\nEjemplo 2. Matriz del grafo A-B-C-D")
    mostrar_matriz(vertices, matriz)


def ejemplo_operaciones_basicas():
    grafo = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    print("\nEjemplo 3. Agregar vértices, aristas y consultar vecinos")
    agregar_vertice(grafo, "D")
    agregar_arista(grafo, "A", "D")
    mostrar_grafo(grafo)
    print("Vecinos de Managua:", consultar_vecinos(grafo, "A"))
    print("¿Existe la arista A-D?", existe_arista(grafo, "A", "D"))


def ejemplo_eliminaciones():
    grafo = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    print("\nEjemplo 4. Eliminar aristas y vértices en clases")
    eliminar_arista(grafo, "A", "B")
    print("Después de eliminar A-B:", grafo)
    eliminar_vertice(grafo, "C")
    print("Después de eliminar C:", grafo)


def ejemplo_grafo_ponderado():
    rutas = {
        "A": {"B": 12, "C": 20},
        "B": {"A": 12, "C": 7},
        "C": {"A": 20, "B": 7},
    }
    print("\nEjemplo 5. Consultar el costo de una conexión directa")
    print("Costo A-C:", costo_directo(rutas, "A", "C"))
    print("Costo A-D:", costo_directo(rutas, "A", "D"))
    print("Costo de A-B-C:", costo_directo(rutas, "A", "B") + costo_directo(rutas, "B", "C"))


if __name__ == "__main__":
    ejemplo_grafo_no_dirigido()
    ejemplo_matriz_adyacencia()
    ejemplo_operaciones_basicas()
    ejemplo_eliminaciones()
    ejemplo_grafo_ponderado()
