"""
Algoritmo de Floyd-Warshall (todos contra todos).
Devuelve:
- nodos: lista ordenada de nodos
- dist: matriz con dist[i][j] = distancia minima de nodos[i] a nodos[j]
- sig:  matriz de "siguiente" para reconstruccion de camino
"""
from math import inf

def _all_nodes_from(grafo: dict) -> list:
    nodes = set(grafo.keys())
    for u, ady in grafo.items():
        nodes.update(ady.keys())
    return sorted(nodes)

def floyd_warshall(grafo: dict):
    nodos = _all_nodes_from(grafo)
    idx = {n: i for i, n in enumerate(nodos)}
    n = len(nodos)

    dist = [[inf] * n for _ in range(n)]
    sig  = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0.0
        sig[i][i]  = nodos[i]

    for u, ady in grafo.items():
        i = idx[u]
        for v, w in ady.items():
            j = idx[v]
            if w < dist[i][j]:
                dist[i][j] = float(w)
                sig[i][j] = v

    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == inf:
                continue
            for j in range(n):
                nd = dik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
                    sig[i][j] = sig[i][k]

    return nodos, dist, sig

def reconstruir_camino(nodos, sig, origen, destino):
    if origen not in nodos or destino not in nodos:
        return None
    i = nodos.index(origen)
    j = nodos.index(destino)
    if sig[i][j] is None:
        return None
    camino = [origen]
    while origen != destino:
        origen = sig[i][j]
        i = nodos.index(origen)
        camino.append(origen)
    return camino

if __name__ == "__main__":
    grafo = {
        'A': {'B': 3, 'C': 8},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {'A': 2}
    }
    nodos, dist, sig = floyd_warshall(grafo)
    print("Nodos:", nodos)
    print("Matriz de distancias minimas:")
    for fila in dist:
        print(fila)
    print("Camino minimo A -> D:", reconstruir_camino(nodos, sig, 'A', 'D'))
