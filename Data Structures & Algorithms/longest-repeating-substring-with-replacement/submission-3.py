class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0
        characters_seen = set()
        for c in s:
            characters_seen.add(c)

        for character in characters_seen:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] != character:
                    count += 1
                while count > k:
                    if s[l] != character:
                        count -= 1
                    l += 1
                max_length = max(r-l+1, max_length)
        return max_length
                
