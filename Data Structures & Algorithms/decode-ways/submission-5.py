class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
            
        res = [0] * len(s)
        res[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                res[i] += res[i-1]
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                res[i] += res[i-2] if i-2 >= 0 else 1
            if res[i] == 0:
                return 0
        return res[-1]
