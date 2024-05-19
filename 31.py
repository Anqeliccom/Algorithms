from collections import defaultdict

class Kosaraju:
    def __init__(self):
        self.graph = defaultdict(list)
        self.reversed_graph = defaultdict(list)
        self.stack = []  # для хранения вершин после завершения DFS
        self.visited_nodes = set()
        self.components = []  # для хранения компонент сильной связности (SCC)

    # построение исходного графа и обратного
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.reversed_graph[v].append(u)

    # запуск DFS на обратном графе
    def fill_stack(self, v):
        self.visited_nodes.add(v)
        for neighbor in self.reversed_graph.get(v, []):
            if neighbor not in self.visited_nodes:
                self.fill_stack(neighbor)
        self.stack.append(v)

    # запуск DFS в исходном графе
    def dfs(self, v, visited_nodes, component):
        visited_nodes.add(v)
        component.append(v)
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited_nodes:
                self.dfs(neighbor, visited_nodes, component)

    def get_components(self):
        # первый проход dfs на обратном графе для заполнения стека
        for v in self.reversed_graph:
            if v not in self.visited_nodes:
                self.fill_stack(v)
        self.visited_nodes.clear()
        
        # второй проход dfs на исходном графе
        while self.stack:
            v = self.stack.pop()
            if v not in self.visited_nodes:
                component = []
                self.dfs(v, self.visited_nodes, component)
                self.components.append(component)
        
        return self.components

def run_kosaraju(graph):
    kosaraju = Kosaraju()
    for u in graph:
        for v in graph[u]:
            kosaraju.add_edge(u, v)
    return kosaraju.get_components()

def check_recursive_calls(components, graph):
    def dfs_rec_check(node, visited_nodes, component):
        visited_nodes.add(node)
        for neighbor in graph.get(node, []):
            if neighbor in component:
                recursive_calls[node] = True
                break
            if neighbor not in visited_nodes:
                dfs_rec_check(neighbor, visited_nodes, component)

    recursive_calls = {}
    for component in components:
        visited_nodes = set()
        for node in component:
            if node not in visited_nodes:
                dfs_rec_check(node, visited_nodes, component)
            if node not in recursive_calls:
                recursive_calls[node] = False
    return recursive_calls

# тест
graph = {
    'foo': ['bar', 'baz', 'qux'],
    'bar': ['baz', 'foo', 'bar'],
    'qux': ['qux'],
    'baz': []
}

components = run_kosaraju(graph)
largest_component = max(components, key=len)
print("Largest recursive component:", largest_component)

recursive_calls = check_recursive_calls(components, graph)
print("\nRecursive calls:")
for function, is_recursive in recursive_calls.items():
    print(f"{function}: {'Yes' if is_recursive else 'No'}")