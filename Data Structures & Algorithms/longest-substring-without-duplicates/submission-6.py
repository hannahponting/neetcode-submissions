class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r = 0, 1
        current_chars = set(s[l])
        max_length = 1
        while r < len(s):
            if s[r] not in current_chars:
                current_chars.add(s[r])
                max_length = max(max_length, r-l+1)
                r += 1
            else:
                current_chars.remove(s[l])
                l +=1
        return max_length