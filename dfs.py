tor = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

rows = len(tor)
cols = len(tor[0])

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

graph = {}

for row in range(rows):
    for col in range(cols):
        if tor[row][col] != '#':
            graph[(row, col)] = []

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if tor[new_row][new_col] != '#':
                        graph[(row, col)].append(((new_row, new_col), 1))


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded = []

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        expanded.append(node)

        if node == goal:
            return path, expanded

        for neighbour, cost in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, expanded


start = (0, 0)
goal = (5, 5)

path, expanded = dfs(graph, start, goal)

print("Табылған жол: ", path)

print("Жолдың құны: ", len(path) - 1)
print("Кеңейтілген түйіндер саны: ", len(expanded))