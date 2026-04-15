from collections import deque

graph = {
    0: [1, 3],
    1: [2, 4],
    3: [5, 7],
    2: [],
    4: [],
    5: [],
    7: [6],
    6: []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(0)