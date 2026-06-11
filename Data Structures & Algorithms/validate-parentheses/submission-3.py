class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in characters.values():
                stack.append(i)
            else:
                if stack and stack[-1] == characters[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True