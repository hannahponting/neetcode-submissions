class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValidPalindrome(s):
            l = 0
            r = len(s)-1

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
                return isValidPalindrome(s[l+1:r+1]) or isValidPalindrome(s[l:r])
        return True