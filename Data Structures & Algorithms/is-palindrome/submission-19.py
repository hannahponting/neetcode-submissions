class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNum(letter):
            if ord('a') <= ord(letter) and ord(letter) <= ord('z'):
                return True
            elif ord('A') <= ord(letter) and ord(letter) <= ord('Z'):
                return True
            elif ord('0') <= ord(letter) and ord(letter) <= ord('9'):
                return True
            else:
                return False

        l = 0
        r = len(s)-1

        while l<r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l +=1
                r -= 1
        return True
                