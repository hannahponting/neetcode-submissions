class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(":")", "{":"}", "[":"]"}

        for i in s:
            if i in openToClose:
                stack.append(i)
            else:
                if stack and openToClose[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                
