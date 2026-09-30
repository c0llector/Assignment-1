from collections import deque
import heapq

tor = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def heuristic(node):
    row, col = node

    return abs(row - goal[0]) + abs(col - goal[1])

def astar(tor):
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic(start), 0, start))

    parent = {start: None}
    g_cost = {start: 0}

    visited = set()

    expanded = 0

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        expanded += 1

        if current == goal:
            break

        row, col = current

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < len(tor)
                and 0 <= nc < len(tor[0])
                and tor[nr][nc] != '#'
            ):
                neighbor = (nr, nc)

                new_g = g + 1

                if (
                    neighbor not in g_cost
                    or new_g < g_cost[neighbor]
                ):
                    g_cost[neighbor] = new_g
                    parent[neighbor] = current

                    h = heuristic(neighbor)
                    f = new_g + h

                    heapq.heappush(
                        priority_queue,
                        (f, new_g, neighbor)
                    )

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    cost = g_cost[goal]

    return path, cost, expanded


astar_path, astar_cost, astar_expanded = astar(tor)

print("Жол:", astar_path)
print("Жол құны:", astar_cost)
print("Кеңейтілген түйіндер:", astar_expanded)