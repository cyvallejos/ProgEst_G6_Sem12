# Representacion inicial del grafo no dirigido.
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"],
}


def mostrar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return []
    return grafo[vertice]


print("Representacion inicial - vecinos de C:", mostrar_vecinos(grafo, "C"))

# Cada arista no dirigida aparece en las listas de sus dos extremos:
# por ejemplo, A-B aparece en grafo["A"] y en grafo["B"]. Por eso,
# para contar aristas se suma el total de vecinos y se divide entre dos.


# Reto 1: Reconoce la estructura
def contar_vertices(grafo):
    return len(grafo)


def contar_aristas(grafo):
    total_vecinos = 0
    for vecinos in grafo.values():
        total_vecinos += len(vecinos)
    return total_vecinos // 2


print("\nReto 1: Reconoce la estructura")
print("Vertices:", contar_vertices(grafo))
print("Aristas:", contar_aristas(grafo))


# Reto 2: Busca conexiones directas
def estan_conectados(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    return destino in grafo[origen]


print("\nReto 2: Busca conexiones directas")
print("A y B:", estan_conectados(grafo, "A", "B"))
print("A y F:", estan_conectados(grafo, "A", "F"))
print("X y A:", estan_conectados(grafo, "X", "A"))


# Reto 3: Amplia la red
def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def agregar_arista(grafo, origen, destino):
    # Las aristas solo se agregan entre vertices existentes. Los lazos
    # se rechazan con ValueError y las aristas repetidas no hacen cambios.
    if origen not in grafo or destino not in grafo:
        raise ValueError("Los dos vertices deben existir en el grafo.")
    if origen == destino:
        raise ValueError("No se permiten lazos (aristas de un vertice a si mismo).")
    if destino not in grafo[origen]:
        grafo[origen].append(destino)
        grafo[destino].append(origen)


# Se usa una copia para que los retos 4 y 5 prueben el grafo inicial.
grafo_ampliado = {vertice: vecinos[:] for vertice, vecinos in grafo.items()}
agregar_vertice(grafo_ampliado, "G")
agregar_arista(grafo_ampliado, "F", "G")
print("\nReto 3: Amplia la red")
print("Vecinos de F:", grafo_ampliado["F"])
print("Vecinos de G:", grafo_ampliado["G"])


# Reto 4: Explora sin repetir (recorrido en amplitud)
def recorrido_amplitud(grafo, inicio):
    if inicio not in grafo:
        return []

    cola = [inicio]
    visitados = [inicio]
    indice = 0

    while indice < len(cola):
        actual = cola[indice]
        indice += 1
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return visitados


print("\nReto 4: Explora sin repetir")
print("Recorrido desde A:", recorrido_amplitud(grafo, "A"))


# Reto 5: Encuentra una ruta
def existe_ruta(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino:
        return True

    cola = [origen]
    visitados = [origen]
    indice = 0

    while indice < len(cola):
        actual = cola[indice]
        indice += 1
        for vecino in grafo[actual]:
            if vecino == destino:
                return True
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return False


print("\nReto 5: Encuentra una ruta")
print("Ruta A-F:", existe_ruta(grafo, "A", "F"))
print("Ruta A-A:", existe_ruta(grafo, "A", "A"))
print("Ruta A-X:", existe_ruta(grafo, "A", "X"))


# Autoevaluacion
# Pregunta: Que dificultad encontraste y como la resolviste?
# Respuesta: Me costo contar las aristas porque cada arista no dirigida
# aparece en las listas de los dos vertices que conecta. Lo resolvi sumando
# las listas de vecinos y dividiendo el total entre dos.
