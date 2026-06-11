class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}
        response = ""
        response_count = float('infinity')

        for i in t:
            need[i] = need.get(i, 0) + 1
            have[i] = 0
        needcount = len(need)
        havecount = 0

        j = 0
        for i in range(0, len(s)):
            if i == 0:
                if s[i] in need:
                    have[s[i]] += 1
                    if have[s[i]] == need[s[i]]:
                        havecount += 1
            else:
                if s[i-1] in need:
                    have[s[i-1]] -=1
                    if have[s[i-1]] == need[s[i-1]] -1:
                        havecount -= 1
            while needcount != havecount and j != len(s)-1:
                j += 1
                if s[j] in need:
                    have[s[j]] += 1
                    if have[s[j]] == need[s[j]]:
                        havecount += 1
            if havecount == needcount and len(s[i:j+1]) < response_count:
                response = s[i:j+1]
                response_count = len(response)
        return response
            