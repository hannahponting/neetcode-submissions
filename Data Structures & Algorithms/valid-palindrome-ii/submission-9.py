class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isValidPalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] == word[r]:
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
                if not isValidPalindrome(s[l+1:r+1]) and not isValidPalindrome(s[l:r]):
                    return False
                else:
                    return True
        return True