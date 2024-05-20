from collections import defaultdict

class Solution:
    def sortItems(self, n, m, group, before_items):
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1
        
        item_dep = defaultdict(list)
        group_dep = defaultdict(list)
        
        for i in range(n):
            for previous in before_items[i]:
                item_dep[previous].append(i)
                if group[previous] != group[i]: # если элементы принадлежат разным группам 
                    group_dep[group[previous]].append(group[i])

        def dfs(graph, node, visited, result, counter):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if not dfs(graph, neighbor, visited, result, counter):
                        return False # цикл в подграфе, достижимым из neighbor
                elif neighbor not in result:
                    return False  # вершина была посещена, но не добавлена в результат - обнаружен цикл
            result.append(node)
            counter -= 1
            return True
        
        # топологическая сортировка для групп
        group_visited = [False] * new_group_id
        group_res = []
        group_counter = new_group_id
        for i in range(new_group_id):
            if not group_visited[i]:
                if not dfs(group_dep, i, group_visited, group_res, group_counter):
                    return [] # если нашли цикл, то возвращаем пустой список 
        group_res.reverse()
        
        # топологическая сортировка для элементов
        item_visited = [False] * n
        item_res = []
        item_counter = n
        for i in range(n):
            if not item_visited[i]:
                if not dfs(item_dep, i, item_visited, item_res, item_counter):
                    return [] # если нашли цикл, то возвращаем пустой список 
        item_res.reverse()
        
        # строим результат
        group_to_items = defaultdict(list)
        for i in range(n):
            group_to_items[group[i]].append(i) # добавляем элемент в соответствующую группу
        
        item_pos = {item: pos for pos, item in enumerate(item_res)}
        result = []
        for i in group_res:
            items = group_to_items[i]
            items.sort(key=lambda x: item_pos[x])
            result.extend(items)
        
        return result

# тесты
solution = Solution()

n1 = 8
m1 = 2
group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
before_items1 = [[], [6], [5], [6], [3, 6], [], [], []]
result1 = solution.sortItems(n1, m1, group1, before_items1)
print(result1) # [6, 3, 4, 1, 5, 2, 0, 7]

n2 = 8
m2 = 2
group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
before_items2 = [[], [6], [5], [6], [3], [], [4], []]
result2 = solution.sortItems(n2, m2, group2, before_items2)
print(result2) # []

n3 = 5
m3 = 5
group3 = [2, 0, -1, 3, 0]
before_items3 = [[2, 1, 3], [2, 4], [], [], []]
result3 = solution.sortItems(n3, m3, group3, before_items3)
print(result3) # [3, 2, 4, 1, 0]