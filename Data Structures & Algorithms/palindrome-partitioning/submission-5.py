class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i, subset):
            if i == len(s):
                res.append(subset[::])
            
            for j in range(i, len(s)):
                if isPalin(i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1, subset)
                    subset.pop()

        dfs(0, [])
        return res