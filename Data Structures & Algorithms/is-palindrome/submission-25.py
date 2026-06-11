class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(letter):
            if ord('A') <= ord(letter) <= ord('Z') or ord('a') <= ord(letter) <= ord('z') or ord('0') <= ord(letter) <= ord('9'):
                return True
            else:
                return False
            
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l<r and not isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True