class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        letters = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}

        def dfs(i, subset):
            if i == len(digits):
                res.append("".join(subset[::]))
                return
            
            for j in letters[digits[i]]:
                subset.append(j)
                dfs(i+1, subset)
                subset.pop()

        dfs(0, [])
        return res