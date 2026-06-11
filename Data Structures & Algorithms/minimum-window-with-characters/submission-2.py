class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}

        for i in t:
            need[i] = need.get(i, 0) + 1
            have[i] = 0
        have_count = 0
        need_count = len(need)
        response = ""
        response_count = float('infinity')

        i = 0
        for j in range(len(s)):
            right_char = s[j]
            if right_char in need:
                have[right_char] +=1
                if have[right_char] == need[right_char]:
                    have_count +=1

            while have_count == need_count:
                if len(s[i:j+1])<response_count:
                    response_count = len(s[i:j+1])
                    response = s[i:j+1]
                left_char = s[i]
                if left_char in need:
                    if have[left_char] == need[left_char]:
                        have_count -= 1
                    have[left_char] -= 1
                i += 1
        return response



