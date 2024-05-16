def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n

    def dfs(node, color):
        stack = [(node, color)]

        while stack:
            node, color = stack.pop()

            if colors[node] == -1:
                colors[node] = color
                for neighbor in graph[node]:
                    stack.append((neighbor, 1 - color))
            else:
                if colors[node] != color:
                    return False

        return True

    for start in range(n):
        if colors[start] == -1:
            if not dfs(start, 0):
                return False

    return True

graph1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(is_bipartite(graph1)) # False
print(is_bipartite(graph2)) # True
