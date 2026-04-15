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


# Graph 2 (middle diagram)
graph2 = {
    'V1': [('V2', 4)],
    'V2': [('V3', 2), ('V4', 7), ('V5', 3)],
    'V3': [('V5', 1)],
    'V4': [('V5', 1), ('V6', 1)],
    'V5': [],
    'V6': []
}

ucs(graph2, 'V1', 'V6')