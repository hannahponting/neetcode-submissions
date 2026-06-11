class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_nums_s = [0]*26
        seen_nums_t = [0]*26

        for i in range(len(s)):
            seen_nums_s[ord(s[i])-ord('a')] = seen_nums_s[ord(s[i])-ord('a')] + 1
            seen_nums_t[ord(t[i])-ord('a')] = seen_nums_t[ord(t[i])-ord('a')] + 1
        return seen_nums_s == seen_nums_t

        
