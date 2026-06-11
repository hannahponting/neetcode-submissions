class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = [0]*26
        t_char = [0]*26

        for i in s:
            s_char[ord(i)-ord('a')] +=1
        for i in t:
            t_char[ord(i)-ord('a')] +=1
        
        return s_char == t_char