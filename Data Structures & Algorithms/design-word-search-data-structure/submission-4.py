class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        tree = self.root
        for w in word:
            if w not in tree.children:
                tree.children[w] = Trie()
            tree = tree.children[w]
        tree.word = True

    def search(self, word: str) -> bool:
        
        def dfs(i, tree):
            if i == len(word):
                return tree.word
            if word[i] != '.':
                if word[i] not in tree.children:
                    return False
                return dfs(i+1, tree.children[word[i]])
            else:
                for child in tree.children:
                    if dfs(i+1, tree.children[child]):
                        return True
                return False
        
        return dfs(0, self.root)
