class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        tree = Trie()
        for word in dictionary:
            tree.addWord(word)
        
        n = len(s)
        dp = {n: 0}

        for i in range(n-1, -1, -1):
            res = dp[i+1]+1
            curr = tree.root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    res = min(res, dp[j+1])
            dp[i] = res
        return dp[0]
        