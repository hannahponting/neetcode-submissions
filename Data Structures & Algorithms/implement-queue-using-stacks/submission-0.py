class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        spare = []
        for i in range(len(self.stack)-1):
            spare.append(self.stack.pop())
        value = self.stack[0]
        stack = []
        for i in range(len(spare)):
            stack.append(spare.pop())
        self.stack = stack
        return value
        

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()