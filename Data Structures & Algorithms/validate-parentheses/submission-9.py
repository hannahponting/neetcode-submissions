class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in characters:
                stack.append(i)
            else:
                if not stack or characters[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True