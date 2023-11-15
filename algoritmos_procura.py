import networkx as nx
import matplotlib.pyplot as plt
import sys
from queue import Queue
#.................................................
from queue import Queue

def dijkstra(graph, origem, destino):
    dist = {node: float('inf') for node in graph}
    queue = Queue()
    predecessor = {}
    
    dist[origem] = 0
    queue.put(origem)
    predecessor[origem] = None  # Definir o predecessor do nó de origem como None

    while not queue.empty():
        current_node = queue.get()

        for neighbor in nx.neighbors(graph,current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = dist[current_node] + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                predecessor[neighbor] = current_node
                queue.put(neighbor)

    # Reconstrói o caminho mais curto
    if destino not in predecessor:  # Se não há caminho para o destino
       return float('inf'), []
    
    path = []
    current = destino
    while current is not None:
        path.append(current)
        current = predecessor[current]

    return dist[destino],path
#..............................................................................

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





