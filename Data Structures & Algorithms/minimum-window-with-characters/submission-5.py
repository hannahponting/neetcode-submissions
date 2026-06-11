class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        #build a hashmap to track exact chars in t
        t_map = defaultdict(int)

        minimum_length = float('inf')
        min_string = ''

        for character in t:
            t_map[character]+= 1
        t_count = len(t_map)
        #eg char_count = 3 where AABBCC is the string 
        # t_map = {'A':2, 'B':2, 'C':2}

        current_s_count = 0
        current_s_map = defaultdict(int)
        l = 0
        for r in range(len(s)):
            current_s_map[s[r]] += 1
            if t_map[s[r]] == current_s_map[s[r]]:
                current_s_count += 1
            while current_s_count == t_count:
                if len(s[l:r+1]) < minimum_length:
                    minimum_length = len(s[l:r+1])
                    min_string = s[l:r+1]
                if t_map[s[l]] == current_s_map[s[l]]:
                    current_s_count -= 1
                current_s_map[s[l]] -=1
                l +=1
        return min_string
            
        
