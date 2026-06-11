class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maximum_letter = 0
        max_length = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maximum_letter = max(maximum_letter, count[s[r]])

            while (r-l+1) - maximum_letter > k:
                count[s[l]] -= 1
                l += 1
                maximum_letter = max(count.values())
            max_length = max(max_length, r-l+1)
        return max_length
