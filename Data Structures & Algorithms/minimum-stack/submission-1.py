class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum_stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum_stack.append(val)
        else:
            if val < self.minimum_stack[-1]:
                self.minimum_stack.append(val)
            else:
                self.minimum_stack.append(self.minimum_stack[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
        
