class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = {}
        countt = {}
        minwindow = float('inf')
        minstring = ''

        for letter in t:
            countt[letter] = countt.get(letter, 0) + 1
        needed_matches = len(countt.keys())
        current_matches = 0
        print(countt)
        print(needed_matches)

        l = 0
        r = -1
        while r < len(s):
            while current_matches < needed_matches:
                if r ==  len(s) -1: 
                    return minstring
                print(f"invalid so increasing r: {r} -> {r+1}")
                r += 1
                counts[s[r]] = counts.get(s[r], 0) + 1
                if s[r] in countt:
                    if countt[s[r]] == counts.get(s[r], 0):
                        current_matches += 1
            while current_matches == needed_matches:
                if minwindow > r-l+1:
                    minstring = s[l:r+1]
                    minwindow = r-l+1
                if countt.get(s[l], 0) == counts[s[l]]:
                    current_matches -= 1
                counts[s[l]] -= 1
                l += 1
        return minstring
        
