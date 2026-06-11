class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tLetters = defaultdict(int)
        sLetters = defaultdict(int) 

        needed_matches = 0
        current_matches  = 0
        minstring = ''
        minstringlength = float('inf')

        for letter in t:
            tLetters[letter] += 1

        needed_matches = len(tLetters)
        print(needed_matches)

        l = 0

        for r in range(len(s)):
            sLetters[s[r]] += 1
            if s[r] in tLetters and sLetters[s[r]] == tLetters[s[r]]:
                current_matches += 1
            while current_matches == needed_matches:
                if len(s[l:r+1]) < minstringlength:
                    minstringlength = r-l+1
                    minstring = s[l:r+1]
                if s[l] in tLetters and sLetters[s[l]] == tLetters[s[l]]:
                    current_matches -= 1
                sLetters[s[l]] -= 1
                l += 1
        return minstring

