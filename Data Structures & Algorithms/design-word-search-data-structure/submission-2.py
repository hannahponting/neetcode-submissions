class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.trie

        for w in word:
            idx = ord(w) - ord('a')

            if not root.children[idx]:
                root.children[idx] = TrieNode()

            root = root.children[idx]

        root.end = True

    def search(self, word: str) -> bool:
        def dfs(i, tree):
            if i == len(word):
                return tree.end
            
            if word[i] == '.':
                for child in tree.children:
                    if child and dfs(i+1, child):
                        return True
                return False
            
            if not tree.children[ord(word[i])-ord('a')]:
                return False
            return dfs(i+1, tree.children[ord(word[i])-ord('a')])
        return dfs(0, self.trie)