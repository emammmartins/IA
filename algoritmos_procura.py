import networkx as nx
import matplotlib.pyplot as plt
import sys
from queue import Queue

def dijkstra(graph, start, end):
    dist = nx.shortest_path_length(graph, source=start, target=end, weight='distancia')
    path = nx.shortest_path(graph, source=start, target=end, weight='distancia')
    return dist, path

def procura_em_profundidade(grafo, inicio, destino):
    if inicio == destino:
        return [inicio], 0

    pilha = [(inicio, [inicio])]  # Pilha para armazenar o nó atual e o caminho percorrido
    visitados = set()  # Conjunto para armazenar os nós visitados

    while pilha:
        (no_atual, caminho) = pilha.pop()

        if no_atual not in visitados:
            vizinhos = list(grafo.neighbors(no_atual))
            for vizinho in vizinhos:
                novo_caminho = caminho.copy()
                novo_caminho.append(vizinho)
                pilha.append((vizinho, novo_caminho))

                if vizinho == destino:
                    custo_total = sum(grafo[no_atual][vizinho]['weight'] for no_atual, vizinho in zip(novo_caminho, novo_caminho[1:]))
                    #print(novo_caminho)
                    #print(custo_total)
                    return novo_caminho, custo_total

            visitados.add(no_atual)

    return None  # Retorna None se não encontrar um caminho


def bfs (graph, start, end):
    
    #fila de nodos a visitar
    queue = Queue()
    queue.put(start)

    #Nodos já visitados
    visitados = set()
    visitados.add(start)

    #nodos anteriores (permite guardar o path)
    pais = dict()
    pais[start] = None

    atual = queue.get()
    while not queue.empty() and atual != end:
        for adjacente in graph[atual]:
            if adjacente not in visitados:
                pais[adjacente] = atual
                queue.put(adjacente)
                visitados.add(adjacente)
        atual = queue.get()

    path = []
    custo = 0
    if (atual==end):
        path.append(end)
        while pais[end] != None: #is not
            end = pais[end]
            path.append(end)
        path.reverse()
        # funçao calcula custo caminho
        #custo = graph.calcula_custo(path)

    return (path, custo)
