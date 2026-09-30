import heapq

tor = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

graph = {}

for row in range(len(tor)):
    for col in range(len(tor[0])):
        if tor[row][col] != '#':
            graph[(row, col)] = []

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < len(tor)
                    and 0 <= nc < len(tor[0])
                    and tor[nr][nc] != '#'
                ):
                    graph[(row, col)].append(((nr, nc), 1))


def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    expanded = []

    while frontier:
        g, node, path = heapq.heappop(frontier)

        if g != best_cost.get(node):
            continue

        expanded.append(node)

        if node == goal:
            return path, g, expanded

        for neighbour, step_cost in graph[node]:
            new_g = g + step_cost

            if new_g < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_g

                heapq.heappush(
                    frontier,
                    (new_g, neighbour, path + [neighbour])
                )

    return None, float("inf"), expanded


path, cost, expanded = ucs(graph, start, goal)

print("Жол:", path)
print("Жол құны:", cost)
print("Кеңейтілген түйіндер саны:", len(expanded))