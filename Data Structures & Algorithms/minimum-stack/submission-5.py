class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.current_min[-1]:
            self.current_min.append(val)
        else:
            self.current_min.append(self.current_min[-1])
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.current_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[-1]
        
