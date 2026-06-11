class Trie:
    def __init__(self):
        self.children = {}
        self.word = False


class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        tree = self.root
        for w in word:
            if w not in tree.children:
                tree.children[w] = Trie()
            tree = tree.children[w]
        tree.word = True

    def search(self, word: str) -> bool:
        tree = self.root
        for w in word:
            if w not in tree.children:
                return False
            tree = tree.children[w]
        return tree.word

    def startsWith(self, prefix: str) -> bool:
        tree = self.root
        for w in prefix:
            if w not in tree.children:
                return False
            tree = tree.children[w]
        return True
        
        