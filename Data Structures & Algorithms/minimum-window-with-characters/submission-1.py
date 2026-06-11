class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        have = defaultdict(int)
        need = defaultdict(int)
        have_count = 0
        need_count = 0
        response, response_count = "", float("infinity")

        for c in t:
            need[c] += 1
        
        need_count = len(need)
        print(need)
        i, j = 0, -1

        while i < len(s):
            while have_count != need_count and j< len(s)-1:
                j += 1
                char = s[j]
                if char in need:
                    have[char] += 1
                    if have[char] == need[char]:
                        have_count +=1
            if have_count == need_count and len(s[i:j+1])<response_count:
                response = s[i:j+1]
                response_count = len(s[i:j+1])
                print(response)

            if s[i] in need:
                if have[s[i]] == need[s[i]]:
                    have_count -= 1
                have[s[i]] -= 1
            i +=1
        return response