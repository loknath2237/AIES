# Graph 4
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [],
    5: [],
    6: [],
    7: [],
    8: []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

dfs(1)