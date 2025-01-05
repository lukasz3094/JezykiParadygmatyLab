graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['A'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs_shortest_path(graph, start, end):
    queue = []
    queue.append([start])

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            return path

        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print(bfs_shortest_path(graph, 'A', 'F'))