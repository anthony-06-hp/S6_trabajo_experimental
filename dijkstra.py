"""
Implementación del algoritmo de Dijkstra para grafos con pesos positivos o cero.
El programa calcula:
- distancias: distancia mínima desde el nodo inicial hacia los demás nodos.
- anteriores: nodo previo utilizado para reconstruir cada ruta.
"""

from heapq import heappush, heappop
from math import inf


def obtener_nodos(grafo: dict) -> set:
    conjunto_nodos = set(grafo.keys())

    for nodo, vecinos in grafo.items():
        conjunto_nodos.update(vecinos.keys())

    return conjunto_nodos


def comprobar_pesos_validos(grafo: dict) -> None:
    for origen, vecinos in grafo.items():
        for destino, peso in vecinos.items():
            if peso < 0:
                raise ValueError(
                    f"El algoritmo de Dijkstra no acepta pesos negativos. "
                    f"Arista ({origen!r} -> {destino!r}) con peso {peso!r}"
                )


def calcular_dijkstra(grafo: dict, nodo_inicio, nodo_final=None):
    comprobar_pesos_validos(grafo)

    nodos = obtener_nodos(grafo)

    distancias = {nodo: inf for nodo in nodos}
    anteriores = {nodo: None for nodo in nodos}

    distancias[nodo_inicio] = 0.0

    cola_prioridad = [(0.0, nodo_inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heappop(cola_prioridad)

        if distancia_actual != distancias[nodo_actual]:
            continue  # Se ignora si ya existe una mejor distancia registrada

        if nodo_final is not None and nodo_actual == nodo_final:
            break

        for vecino, peso in grafo.get(nodo_actual, {}).items():
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual
                heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias, anteriores


def formar_camino(anteriores: dict, nodo_inicio, nodo_final):
    if nodo_final not in anteriores:
        return None

    ruta = []
    nodo = nodo_final

    while nodo is not None:
        ruta.append(nodo)
        nodo = anteriores[nodo]

    ruta.reverse()

    if ruta and ruta[0] == nodo_inicio:
        return ruta

    return None


if __name__ == "__main__":
    red = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 6, 'D': 1},
        'C': {'A': 5, 'B': 6, 'D': 2, 'E': 5},
        'D': {'B': 1, 'C': 2, 'E': 1},
        'E': {'C': 5, 'D': 1}
    }

    distancias, anteriores = calcular_dijkstra(red, 'A')

    print("Distancias mínimas partiendo desde A:")

    for nodo in sorted(distancias):
        print(f"A -> {nodo}: {distancias[nodo]}")

    print("Ruta más corta de A hacia E:", formar_camino(anteriores, 'A', 'E'))
