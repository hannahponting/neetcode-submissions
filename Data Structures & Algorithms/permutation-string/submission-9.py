class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1count = defaultdict(int)
        s2count = defaultdict(int)
        nonmatches = 0

        for i in s1:
            s1count[i] +=1

        for i in s2[:len(s1)]:
            s2count[i] += 1

        
        nonmatches = 0
        for i in range(26):
            c = chr(ord('a')+i)
            if s1count[c] != s2count[c]:
                nonmatches +=1
        if nonmatches == 0:
            return True
        for i in range(len(s2)-len(s1)):
            left = s2[i]
            right = s2[i+len(s1)]
            if s2count[left] == s1count[left]:
                nonmatches += 1
            s2count[left] -=1
            if s2count[left] == s1count[left]:
                nonmatches -= 1


            if s2count[right] == s1count[right]:
                nonmatches +=1
            s2count[right] += 1
            if s2count[right] == s1count[right]:
                nonmatches -= 1
            if nonmatches == 0:
                return True
        return False
            
        
