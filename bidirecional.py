import networkx as nx
from queue import Queue

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start], 0

    forward_visited = set()
    backward_visited = set()

    forward_queue = Queue()
    backward_queue = Queue()

    forward_parent = {start: None}
    backward_parent = {goal: None}

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
            return path, len(path) - 1

        for neighbor in graph.neighbors(forward_current):
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_parent[neighbor] = forward_current
                forward_queue.put(neighbor)

        for neighbor in graph.neighbors(backward_current):
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_parent[neighbor] = backward_current
                backward_queue.put(neighbor)

    return None, float('inf')

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