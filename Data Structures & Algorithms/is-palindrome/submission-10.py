class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while r >l:
            if not self.isAlphaNum(s[l]):
                l += 1
            elif not self.isAlphaNum(s[r]):
                r -= 1
            elif s[r].lower() != s[l].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def isAlphaNum(self, letter):
        if ord('A') <= ord(letter) <= ord('Z'):
            return True
        if ord('a') <= ord(letter) <= ord('z'):
            return True
        if ord('0') <= ord(letter) <= ord('9'):
            return True
            
            