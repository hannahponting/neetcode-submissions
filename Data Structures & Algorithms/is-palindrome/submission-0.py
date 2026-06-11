class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        reverse = s[::-1]
        if reverse == s:
            return True
        return False