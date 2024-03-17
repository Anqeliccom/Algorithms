class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        self.heap.append((priority, item))
        self.sifting_up(len(self.heap) - 1)
        
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        root_el = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self.sifting_down(0)
        return root_el

    def peek_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0

    def sifting_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2 # индекс родительского элемента для текущего
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def sifting_down(self, index):
        while 2 * index + 1 < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_child_index = left_child_index
            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index][0] < self.heap[left_child_index][0]):
                min_child_index = right_child_index
            if self.heap[min_child_index][0] < self.heap[index][0]:
                self.heap[index], self.heap[min_child_index] = \
                    self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

class Solution(object):
    def mergeKLists(self, lists):
        queue = PriorityQueue()

        for head in lists:
            if head:
                queue.insert(head, head.val)

        result = ListNode()
        current = result

        while not queue.is_empty():
            node = queue.extract_min()
            current.next = node
            current = current.next

            if node.next:
                queue.insert(node.next, node.next.val)

        return result.next

def array_to_list(arr):
    head = ListNode()
    current = head
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return head.next

def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [array_to_list(lst) for lst in lists]
result = Solution().mergeKLists(lists)
print(list_to_array(result))
