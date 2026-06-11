class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tLetters = {}
        sLetters = {}
        l = 0
        r = 0
        minlength = float('inf')
        minstring = ''

        for letter in t:
            tLetters[ord(letter)-ord('A')] = tLetters.get(ord(letter)-ord('A'), 0) + 1
    
        needed = len(tLetters.keys())
        print(needed)
        have = 0

        for r in range(len(s)):
            sLetters[ord(s[r])-ord('A')] = sLetters.get(ord(s[r])-ord('A'), 0) + 1
            if ord(s[r])-ord('A') in tLetters and sLetters[ord(s[r])-ord('A')] == tLetters[ord(s[r])-ord('A')]:
                have += 1
            while have == needed:
                print('got here')
                if minlength > r-l+1:
                    minlength = (r-l+1)
                    minstring = s[l:r+1]
                if ord(s[l])-ord('A') in tLetters and sLetters[ord(s[l])-ord('A')] == tLetters[ord(s[l])-ord('A')]:
                    have -= 1
                sLetters[ord(s[l])-ord('A')] -= 1
                l += 1
            print(sLetters)
        return minstring

        
    
