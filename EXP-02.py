from collections import deque

graph = {
    1: [23, 45],
    23: [],
    45: []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            # print each digit separately
            for digit in str(node):
                print(digit, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(1)