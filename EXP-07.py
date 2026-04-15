# Graph 2
graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

dfs(1)