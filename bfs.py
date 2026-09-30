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

def bfs(tor):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    expanded = 0

    while queue:
        current = queue.popleft()
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
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    cost = len(path) - 1
    return path, cost, expanded


bfs_path, bfs_cost, bfs_expanded = bfs(tor)

print("Жол:", bfs_path)
print("Жол құны:", bfs_cost)
print("Кеңейтілген түйіндер:", bfs_expanded)