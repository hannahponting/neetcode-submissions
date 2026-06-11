class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                new = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(new))
            elif i == "-":
                new = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(new))
            elif i == "*":
                new = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(new))
            elif i == "/":
                new = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(new))
            else:
                stack.append(int(i))
        return stack[-1]