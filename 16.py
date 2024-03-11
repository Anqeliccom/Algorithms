class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        pointer1 = pointer2 = head

        while pointer2 and pointer2.next: # пока есть куда перемещаться
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            pointer2 = pointer2.next
            if pointer1 == pointer2: # нашли цикл
                break

        if pointer2 is None or pointer2.next is None:
            return None  # нет цикла

        pointer1 = head
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1 # возвращаем индекс узла, с которого цикл начинается




first1 = ListNode(3)
first2 = ListNode(2)
first3 = ListNode(0)
fourth1 = ListNode(-4)
first1.next = first2
first2.next = first3
first3.next = fourth1
fourth1.next = first2

second1 = ListNode(1)
second2 = ListNode(2)
second1.next = second2
second2.next = second1

third1 = ListNode(1)

solution = Solution()
print(solution.detectCycle(first1))
print(solution.detectCycle(second1))
print(solution.detectCycle(third1))
