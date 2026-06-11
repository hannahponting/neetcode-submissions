class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 1
        for l in range(len(s)):
            seen_characters = set(s[l])
            r = l + 1
            while r != len(s) and s[r] not in seen_characters:
                seen_characters.add(s[r])
                max_length = max(max_length, len(s[l:r+1]))
                r += 1
            seen_characters.remove(s[l])
        return max_length