class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_matches = defaultdict(int)
        for i in t:
            t_matches[i] += 1
        num_matches = len(t_matches)
        s_matches = defaultdict(int)

        shortest_string = ""
        length_string = float('inf')

        current_count = 0
        l = 0
        for r in range(len(s)):
            if s[r] in t_matches:
                s_matches[s[r]] += 1
                if s_matches[s[r]] == t_matches[s[r]]:
                    current_count +=1

            while current_count == num_matches:
                if len(s[l:r+1]) <length_string:
                    shortest_string = s[l:r+1]
                    length_string = len(shortest_string)
                
                if s[l] in t_matches:
                    if s_matches[s[l]] == t_matches[s[l]]:
                        current_count -=1  
                    s_matches[s[l]] -= 1
                l += 1
        return shortest_string

                        
                


