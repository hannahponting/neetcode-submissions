class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_characters = [0] * 26
        for i in s1:
            s1_characters[ord(i)- ord('a')] += 1
        s2_characters = [0] * 26
        s2_characters[ord(s2[0]) - ord('a')] += 1
        r = 0
        for l in range(len(s2)):
            while r-l < len(s1)-1 and r < len(s2)-1:
                r += 1
                s2_characters[ord(s2[r])- ord('a')] += 1
            if s2_characters == s1_characters: 
                return True
            s2_characters[ord(s2[l])- ord('a')] -= 1 
        return False



