class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters = [0]*26
        tletters = [0]*26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sletters[ord(s[i])-ord('a')] += 1
            tletters[ord(t[i])-ord('a')] += 1
        return sletters == tletters
