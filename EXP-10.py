# Graph 5
graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: [4],
    4: [5],
    5: [7, 6],
    6: [],
    7: []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

dfs(0)