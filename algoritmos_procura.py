import networkx as nx
import matplotlib.pyplot as plt
import sys

def dijkstra(graph, start, end):
    dist = nx.shortest_path_length(graph, source=start, target=end, weight='distancia')
    path = nx.shortest_path(graph, source=start, target=end, weight='distancia')
    return dist, path





