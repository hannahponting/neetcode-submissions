class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while (i-l+1) - max(count.values())>k:
                count[s[l]] = count[s[l]] -1
                l = l+1
            res = max(res, i-l +1)
        return res