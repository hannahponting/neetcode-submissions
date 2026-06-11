class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = [0] * 26
        for index in range(len(s)):
            seen[ord(s[index])- ord('a')] += 1
            seen[ord(t[index])-ord('a')] -=1
        
        for i in seen:
            if i != 0:
                return False
        return True
