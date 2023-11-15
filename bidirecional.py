from collections import deque

def build_path(graph, start, goal, meeting_point, parent_start, parent_goal):
    path_start = []
    distance_start = 0  
    current = meeting_point
    while current is not None:
        path_start.insert(0, current)
        if parent_start[current] is not None:
            distance_start += graph[parent_start[current]][current]['weight']
        current = parent_start[current]

    path_goal = []
    distance_goal = 0 
    current = parent_goal[meeting_point]
    while current is not None:
        path_goal.append(current)
        if parent_goal[current] is not None:
            distance_goal += graph[parent_goal[current]][current]['weight']
        current = parent_goal[current]

    path = path_start + path_goal
    distance = distance_start + distance_goal

    return path, distance

def bidirectional_search(graph, start, goal):
    start_queue = deque([(start, None)])
    goal_queue = deque([(goal, None)])

    start_explored = set()
    goal_explored = set()

    while start_queue and goal_queue:
        # Expand forward from the start
        current_start, parent_start = start_queue.popleft()
        start_explored.add(current_start)
        if current_start == goal or current_start in goal_explored:
            # Handle meeting point case
            if current_start == goal:
                return build_path(graph, start, goal, current_start, parent_start, {})
            else:
                return build_path(graph, start, goal, current_start, parent_start, goal_queue)

        # Expand backward from the goal
        current_goal, parent_goal = goal_queue.popleft()
        goal_explored.add(current_goal)
        if current_goal == start or current_goal in start_explored:
            return build_path(graph, start, goal, current_goal, start_queue, parent_goal)

        # Expand neighbors from the start
        start_neighbors = list(graph.neighbors(current_start))
        for neighbor in start_neighbors:
            if neighbor not in start_explored:
                start_queue.append((neighbor, current_start))

        # Expand neighbors from the goal
        goal_neighbors = list(graph.neighbors(current_goal))
        for neighbor in goal_neighbors:
            if neighbor not in goal_explored:
                goal_queue.append((neighbor, current_goal))

    return None, 0  # No path found