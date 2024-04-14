class FreqStack:

    def __init__(self):
        self.dict = {}
        self.same_freq = {}
        self.maxfr = 0

    def push(self, val):
        self.dict[val] = self.dict.get(val, 0) + 1 
        freq = self.dict[val]
        if freq not in self.same_freq:
            self.same_freq[freq] = []
        self.same_freq[freq].append(val)
        self.maxfr = max(self.maxfr, freq)

    def pop(self):
        val = self.same_freq[self.maxfr].pop()
        self.dict[val] -= 1
        if not self.same_freq[self.maxfr]:
            del self.same_freq[self.maxfr]
            self.maxfr -= 1
        return val

freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())