import networkx as nx
import matplotlib.pyplot as plt
import sys

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





