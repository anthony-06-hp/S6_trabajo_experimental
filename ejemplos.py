from dijkstra import dijkstra, reconstruir_camino as camino_dijkstra
from floyd_warshall import floyd_warshall, reconstruir_camino as camino_fw
from bfs import bfs_camino

def demo_dijkstra():
    grafo = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 6, 'D': 1},
        'C': {'A': 5, 'B': 6, 'D': 2, 'E': 5},
        'D': {'B': 1, 'C': 2, 'E': 1},
        'E': {'C': 5, 'D': 1}
    }
    dist, prev = dijkstra(grafo, 'A')
    objetivo = 'E'
    print("== Dijkstra ==")
    print("Distancias:", dist)
    print("Camino A -> E:", camino_dijkstra(prev, 'A', 'E'))

def demo_floyd():
    grafo = {
        'A': {'B': 3, 'C': 8},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {'A': 2}
    }
    nodos, dist, sig = floyd_warshall(grafo)
    print("\n== Floyd-Warshall ==")
    print("Nodos:", nodos)
    for fila in dist:
        print(fila)
    print("Camino minimo A -> D:", camino_fw(nodos, sig, 'A', 'D'))

def demo_bfs():
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("\n== BFS ==")
    print("Camino BFS A -> F:", bfs_camino(grafo, 'A', 'F'))

if __name__ == "__main__":
    demo_dijkstra()
    demo_floyd()
    demo_bfs()
