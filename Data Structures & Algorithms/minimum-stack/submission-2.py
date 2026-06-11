class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_mins:
            new_min = min(self.stack_mins[-1], val)
        else:
            new_min = val
        self.stack_mins.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mins[-1]
