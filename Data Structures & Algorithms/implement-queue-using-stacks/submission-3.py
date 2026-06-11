class MyQueue:

    def __init__(self):
        self.stack1= []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            i = self.stack1.pop()
            self.stack2.append(i)
        value = self.stack2.pop()
        while self.stack2:
            i = self.stack2.pop()
            self.stack1.append(i)
        return value

        

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return True if not self.stack1 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()