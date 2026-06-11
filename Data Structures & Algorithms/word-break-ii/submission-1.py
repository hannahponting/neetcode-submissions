class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        sub = []

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(sub))
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()

        backtrack(0)
        return res