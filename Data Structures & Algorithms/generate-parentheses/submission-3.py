class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openP, closeP, subset):
            if openP == closeP == n:
                res.append("".join(subset))
            
            if openP < n:
                subset.append("(")
                backtrack(openP+1, closeP, subset)
                subset.pop()
            if openP > closeP:
                subset.append(")")
                backtrack(openP, closeP+1, subset)
                subset.pop()

        backtrack(0, 0, [])
        return res