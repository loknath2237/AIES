from collections import deque

graph = {
    1: [2, 3],
    2: [5, 6],
    3: [7],
    5: [],
    6: [],
    7: [4, 8],
    4: [],
    8: []
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

bfs(1)