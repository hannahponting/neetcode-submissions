class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = set(s)
        max_length = 0

        for c in characters:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l+1) -count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                max_length = max(max_length, r-l+1)
        return max_length
                
