from collections import deque

graph = {
    1: [2, 7],
    2: [3, 6],
    7: [8, 10],
    3: [4],
    6: [5],
    8: [],
    10: [],
    4: [],
    5: [],
    9: []
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