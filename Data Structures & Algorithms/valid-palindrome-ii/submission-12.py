class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValidPalindrome(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                    l += 1
                    r -= 1
            else:
                return isValidPalindrome(l+1, r) or isValidPalindrome(l, r-1)
        return True