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
        return path, cost

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


