import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            print("Cost:", cost)
            print("Path:", " -> ".join(path))
            return

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbor, path))


# Graph 3 (bottom diagram)
graph3 = {
    'S': [('A', 3), ('B', 2), ('C', 7)],
    'A': [('D', 3), ('E', 8), ('G', 15)],
    'B': [('G', 20)],
    'C': [('G', 6)],
    'D': [],
    'E': [],
    'G': []
}

ucs(graph3, 'S', 'G')