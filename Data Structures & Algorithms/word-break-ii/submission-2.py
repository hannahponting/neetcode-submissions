class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []

        def backtrack(i, subset):
            if i == len(s):
                res.append(" ".join(subset))
                return

            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    subset.append(s[i:j+1])
                    backtrack(j+1, subset)
                    subset.pop()


        backtrack(0, [])
        return res