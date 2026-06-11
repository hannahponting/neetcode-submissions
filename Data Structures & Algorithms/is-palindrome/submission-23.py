class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        def isAlphaNum(character):
            return ord('a') <= ord(character) and ord('z') >= ord(character) or ord('A') <= ord(character) and ord('Z') >= ord(character) or ord('0') <= ord(character) and ord('9') >= ord(character)
        
        while l <= r:
            while l<r and not isAlphaNum(s[l]):
                l += 1
            while l<r and not isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l +=1
                r -= 1
        return True
