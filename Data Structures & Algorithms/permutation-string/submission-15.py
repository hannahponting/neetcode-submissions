class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_characters = [0]*26
        s2_characters = [0]*26

        for index in range(len(s1)):
            s1_characters[ord(s1[index])- ord('a')] += 1
            s2_characters[ord(s2[index])- ord('a')] += 1

        if s1_characters == s2_characters:
            return True
            
        for r in range(len(s1), len(s2)):
            s2_characters[ord(s2[r])- ord('a')] += 1
            s2_characters[ord(s2[r-len(s1)])- ord('a')] -= 1
            if s1_characters == s2_characters:
                return True
        return False


