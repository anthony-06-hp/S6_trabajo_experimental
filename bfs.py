"""
Algoritmo de Búsqueda en Anchura (BFS) aplicado a grafos sin pesos.
Permite encontrar la ruta con menor cantidad de conexiones entre un nodo inicial
y un nodo destino. Si no existe camino, devuelve None.
"""

from collections import deque

def encontrar_ruta_bfs(red: dict, origen, destino):
    if origen not in red:
        raise KeyError(f"El nodo de origen {origen!r} no se encuentra en el grafo")

    nodos_visitados = {origen}
    nodo_anterior = {origen: None}
    pendientes = deque([origen])

    while pendientes:
        actual = pendientes.popleft()

        if actual == destino:
            break

        for vecino in red.get(actual, []):
            if vecino not in nodos_visitados:
                nodos_visitados.add(vecino)
                nodo_anterior[vecino] = actual
                pendientes.append(vecino)

    if destino not in nodo_anterior:
        return None

    # Construcción de la ruta desde el destino hasta el origen
    ruta = []
    nodo = destino

    while nodo is not None:
        ruta.append(nodo)
        nodo = nodo_anterior[nodo]

    ruta.reverse()
    return ruta


if __name__ == "__main__":
    red = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Ruta encontrada con BFS desde A hasta F:", encontrar_ruta_bfs(red, 'A', 'F'))
