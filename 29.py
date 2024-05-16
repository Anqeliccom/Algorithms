class Solution:
    def isBipartite(self, graph):
        colors = {}
        
        def dfs(node, color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            next_color = not color
            return all(dfs(neighbour, next_color) for neighbour in graph[node])

        return all(dfs(node, 1) for node in range(len(graph)) if node not in colors)

graph1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph2 = [[1,3],[0,2],[1,3],[0,2]]

solution = Solution()
print(solution.isBipartite(graph1)) # False
print(solution.isBipartite(graph2)) # True
