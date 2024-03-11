class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if head is None or left == right:
            return head
        
        temp_prev = ListNode(0) # временный предыдущий, чтобы в конце отобразить с начала списка
        temp_prev.next = head
        prev = temp_prev
        
        # находим элемент перед left
        for _ in range(left - 1):
            prev = prev.next
        
        # обращаем интервал
        reverse = None
        cur = prev.next
        for _ in range(right - left + 1):
            next_el = cur.next # сохраняем ссылку на следующий узел
            cur.next = reverse
            reverse = cur
            cur = next_el

        # связываем первый элемент будущей обратимой части с началом части после получившейся обратимой
        prev.next.next = cur
        
        # переключаем первый элемент будущей обратимой части на конец получившейся обратимой части
        prev.next = reverse

        return temp_prev.next

def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

head = ListNode(1)
cur = head
for val in range(2, 13):
    cur.next = ListNode(val)
    cur = cur.next

print("Исходный связный список:")
print_linked_list(head)

left = 3
right = 9

solution = Solution()
new_head = solution.reverseBetween(head, left, right)

print("\nСвязный список в обратном порядке от", left, "до", right, ":")
print_linked_list(new_head)
