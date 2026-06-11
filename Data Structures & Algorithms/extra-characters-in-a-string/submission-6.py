class Tries:

    def __init__(self):
        self.children = {}
        self.word = False

    def build(self, tree, word):
        for w in word:
            if w not in tree.children:
                tree.children[w] = Tries()
            tree = tree.children[w]
        tree.word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        tree = Tries()
        for word in dictionary:
            tree.build(tree, word)
        
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)
            curr = tree
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res

        return dfs(0)




