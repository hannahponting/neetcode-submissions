class FreqStack:

    def __init__(self):
        self.frequencies = defaultdict(list)
        self.counts = defaultdict(int)
        self.maxfrequency = 0

    def push(self, val: int) -> None:
        if self.counts.get(val, None):
            self.counts[val] += 1
        else:
            self.counts[val] = 1
        self.frequencies[self.counts[val]].append(val)
        if self.counts[val] > self.maxfrequency:
            self.maxfrequency = self.counts[val]

    def pop(self) -> int:
        value = self.frequencies[self.maxfrequency].pop()
        self.counts[value] -= 1
        
        if not self.frequencies[self.maxfrequency]:
            self.maxfrequency -= 1

        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()