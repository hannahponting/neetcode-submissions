class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalin(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False  
            return True

        def backtrack(i, subset):
            if i >= len(s):
                res.append(subset.copy())
                return

            for j in range(i, len(s)):
                if isPalin(i, j):
                    subset.append(s[i:j+1])
                    backtrack(j+1, subset)
                    subset.pop()

        backtrack(0, [])
        return res