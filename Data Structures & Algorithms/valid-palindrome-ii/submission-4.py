class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s)-1

        while l < r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                if isPal(l+1,r) or isPal(l, r-1):
                    return True
                else:
                    return False
        return True
