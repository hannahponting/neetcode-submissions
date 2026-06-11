class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{", ")":"(", "]":"["}
        stack = []
        for letter in s:
            if letter in closeToOpen.values():
                stack.append(letter)
            else:
                if stack and closeToOpen.get(letter, '') == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0 

