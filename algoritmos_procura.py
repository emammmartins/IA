import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


def trajeto_completo_estafeta(lista):
    lista_reversa = lista[::-1]  # Reverter a lista
    lista_concatenada = lista + lista_reversa[1:]  # Concatenar a lista original com o seu reverso, excluindo o primeiro elemento do reverso
    return lista_concatenada

def dijkstra(graph, origem, destino):
    dist = {node: float('inf') for node in graph}
    queue = Queue()
    predecessor = {}
    
    dist[origem] = 0
    queue.put(origem)
    predecessor[origem] = None  # Definir o predecessor do nó de origem como None

    while not queue.empty():
        current_node = queue.get()

        for neighbor in nx.neighbors(graph, current_node):
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

    path.reverse()  # Revertendo a lista 'path'

    return trajeto_completo_estafeta(path), dist[destino]

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
                    return trajeto_completo_estafeta(novo_caminho), custo_total

            visitados.add(no_atual)

    return None  # Retorna None se não encontrar um caminho
 #.....................................................................................................

def bfs (graph, start, end):
    if start == end:
        return [start], 0

    #fila de nodos a visitar
    queue = Queue()
    queue.put(start)

    #Nodos já visitados
    visitados = set()
    visitados.add(start)

    #nodos anteriores (permite guardar o path)
    pais = dict()
    pais[start] = None

    #custo para chegar ao nodo
    custo = dict()
    custo[start] = 0

    atual = ""
    while not queue.empty() and atual != end:
        atual = queue.get()
        for adjacente in nx.neighbors(graph,atual):
            peso = graph[atual][adjacente]['weight']
            if adjacente not in visitados:
                queue.put(adjacente)
                pais[adjacente] = atual
                custo[adjacente] = custo[atual] + peso
                visitados.add(adjacente)

    path = []
    c = 0
    if (atual==end):
        c = custo[end]
        path.append(end)
        while pais[end] != None: #is not
            end = pais[end]
            path.append(end)
        path.reverse()
    else:
        return None
    
    return trajeto_completo_estafeta(path), c

#.................................................................
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start], 0

    forward_visited = set()
    backward_visited = set()

    forward_queue = Queue()
    backward_queue = Queue()

    forward_parent = {start: None}
    backward_parent = {goal: None}

    forward_cost = {start: 0}
    backward_cost = {goal: 0}

    forward_queue.put(start)
    backward_queue.put(goal)

    while not forward_queue.empty() and not backward_queue.empty():
        forward_current = forward_queue.get()
        backward_current = backward_queue.get()

        forward_visited.add(forward_current)
        backward_visited.add(backward_current)

        common_node = set(forward_visited) & set(backward_visited)
        if common_node:
            common_node = common_node.pop()
            path = reconstruct_path(forward_parent, backward_parent, common_node)
            total_edge_cost = forward_cost[common_node] + backward_cost[common_node]
            return trajeto_completo_estafeta(path), total_edge_cost

        for neighbor in graph.neighbors(forward_current):
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_parent[neighbor] = forward_current
                forward_cost[neighbor] = forward_cost[forward_current] + graph.get_edge_data(forward_current, neighbor)['weight']
                forward_queue.put(neighbor)

        for neighbor in graph.neighbors(backward_current):
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_parent[neighbor] = backward_current
                backward_cost[neighbor] = backward_cost[backward_current] + graph.get_edge_data(backward_current, neighbor)['weight']
                backward_queue.put(neighbor)

    return None, 0  # No path found

def reconstruct_path(forward_parent, backward_parent, common_node):
    forward_path = []
    backward_path = []

    current = common_node
    while current is not None:
        forward_path.append(current)
        current = forward_parent[current]

    current = common_node
    while current is not None:
        backward_path.append(current)
        current = backward_parent[current]

    return forward_path[::-1] + backward_path[1:]

#......................................................................................
def iterative_deepening_dfs(graph, start, goal):
    if start not in graph or goal not in graph:
        raise ValueError("Start or goal node not in the graph")

    depth_limit = 0

    while True:
        result = depth_limited_dfs(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1


def depth_limited_dfs(graph, current, goal, depth_limit, path=None, cost=0):
    if path is None:
        path = [current]

    if current == goal:
        return trajeto_completo_estafeta(path), cost

    if depth_limit == 0:
        return None

    for neighbor in graph.neighbors(current):
        if neighbor not in path:
            new_path = path + [neighbor]
            new_cost = cost + graph[current][neighbor].get('weight', 1)
            result = depth_limited_dfs(graph, neighbor, goal, depth_limit - 1, new_path, new_cost)
            if result is not None:
                return result

    return None

#.................................................................................................
def greedy_shortest_path(graph, origem, destino):
    cost = 0
    if origem not in graph or destino not in graph:
        return [], float('inf')

    path = []
    current_node = origem
    path.append(current_node)

    while current_node != destino:
        neighbors = list(graph.neighbors(current_node))
        if not neighbors:
            return [], float('inf')

        next_node = None
        min_heuristic = float('inf')

        for neighbor in neighbors:
            heuristic_value = graph.nodes[neighbor]['heuristica'].get(destino, float('inf'))
            if heuristic_value < min_heuristic:
                min_heuristic = heuristic_value
                next_node = neighbor
        
        if next_node is None:
            return [], float('inf')

        path.append(next_node)
        cost += graph[current_node][next_node]['weight']
        current_node = next_node

    return trajeto_completo_estafeta(path), cost
#.............................................................................
def algoritmoAEstrela (graph, origem, destino):
    
    if origem not in graph or destino not in graph:
        return None
    
    # Set de nodos que ainda estamos a verificar
    toCheck = {origem}
    #Set de nodos que já foram verificados
    checked = set()
    # Dicionário de distâncias à origem
    dist = {}
    dist[origem] = 0
    # Dicionário dos nodos anteriores
    pais = {}
    pais[origem] = None
    while len(toCheck)>0:
        
        checking = None
        for node in toCheck:
            if checking == None or (dist[node]+graph.nodes[node]['heuristica'][destino]) < (dist[checking]+graph.nodes[checking]['heuristica'][destino]):
                checking = node
        if checking == destino:
            path = []
            path.append(checking)
            while pais[checking] != None: #is not
                checking = pais[checking]
                path.append(checking)
            path.reverse()
            return trajeto_completo_estafeta(path), dist[destino]
        for n in list(nx.neighbors(graph,checking)):
            if n not in toCheck and n not in checked:
                toCheck.add(n)
                pais[n] = checking
                dist[n] = dist[checking] + graph[checking][n]['weight']
            else: #está numa das listas -> ver se encontramos um caminho mais rápido
                if dist[n] > (dist[checking] + graph[checking][n]['weight']):
                    dist[n] = dist[checking] + graph[checking][n]['weight']
                    pais[n] = checking
                    if n in checked:
                        checked.remove(n)
                        toCheck.add(n)
        toCheck.remove(checking)
        checked.add(checking)
    return None