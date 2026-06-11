class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "{", "["]
        matches = {"}":"{", "]":"[" , ")":"("}
        for character in s:
            if character in open:
                stack.append(character)
            elif stack and matches[character] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        else:
            return False
        