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


# Graph 1 (based on your top diagram)
graph1 = {
    'S': [('A', 1)],
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 1), ('G', 12)],
    'D': [('G', 3)],
    'G': []
}

ucs(graph1, 'S', 'G')