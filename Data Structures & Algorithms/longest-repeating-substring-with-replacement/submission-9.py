class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxcount = 0
        maxlength = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxcount = max(counts[s[r]], maxcount)
            while r-l+1-maxcount > k:
                counts[s[l]] = counts[s[l]] - 1
                l += 1
                maxcount = max(counts.values())
            maxlength = max(maxlength, r-l+1)
        return maxlength
