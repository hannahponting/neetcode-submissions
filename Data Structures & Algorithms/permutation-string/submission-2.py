class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for j in range(len(s1)-1, len(s2)+1):
            print(s2[j-len(s1):j])
            if sorted(s2[j-len(s1):j]) == sorted(s1):
                return True
        return False