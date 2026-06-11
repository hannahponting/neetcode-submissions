class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def backtrack(i, subset):
            d = {"2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
                }
            
            if len(subset) == len(digits):
                res.append("".join(subset))
                return

            for j in d[digits[i]]:
                subset.append(j)
                backtrack(i+1, subset)
                subset.pop()
        if digits:
            backtrack(0, [])
            return res
        else:
            return []



        
