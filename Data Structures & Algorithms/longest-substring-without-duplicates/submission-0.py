class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seenChars = set()

        res = 0

        for i in range(len(s)):
            while s[i] in seenChars:
                print(seenChars)
                seenChars.remove(s[l])
                l = l+1
            seenChars.add(s[i])
        
            res = max(res, i-l +1)
        return res

            