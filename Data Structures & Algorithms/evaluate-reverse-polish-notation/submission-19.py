class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for i in tokens:
            if i == '+':
                a = result.pop()
                b = result.pop()
                result.append(a+b)
            elif i == '*':
                a = result.pop()
                b = result.pop()
                result.append(a*b)
            elif i == '-':                
                a = result.pop()
                b = result.pop()
                result.append(b-a)
            elif i == '/':
                a = result.pop()
                b = result.pop()
                result.append(int(b/a))
            else:
                result.append(int(i))

        return result[0]
