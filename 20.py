class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, el):
        self.stack.append(el)
        if not self.min_stack or el <= self.min_stack[-1]:
            self.min_stack.append(el)

    def pop(self):
        if not self.stack:
            return None
        pop_el = self.stack.pop()
        if pop_el == self.min_stack[-1]:
            self.min_stack.pop()
        return pop_el

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

stack = MinStack()
stack.push(-2)
stack.push(5)
stack.push(2)
stack.push(-3)
print("Минимальный:", stack.getMin())
stack.pop()
print("Минимальный:", stack.getMin()) 
print("Верхний:", stack.top())
