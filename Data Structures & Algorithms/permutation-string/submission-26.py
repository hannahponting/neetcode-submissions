class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        s1letters = [0] *26
        s2letters = [0] *26
        

        for i in range(len(s1)):
            s1letters[ord(s1[i])-ord('a')] += 1
            s2letters[ord(s2[i])-ord('a')] += 1

        r = len(s1)
        while r < len(s2):
            if s1letters == s2letters:
                return True
            else:
                s2letters[ord(s2[r])-ord('a')] += 1
                s2letters[ord(s2[r-len(s1)])-ord('a')] -= 1
                r += 1
            print(s2letters)
        if s1letters == s2letters:
            return True
        return False