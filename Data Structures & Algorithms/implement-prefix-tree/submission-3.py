class Tries:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.tree = Tries()

    def insert(self, word: str) -> None:
        root = self.tree
        for w in word:
            if w not in root.children:
                root.children[w] = Tries()
            root = root.children[w]
        root.word = True

    def search(self, word: str) -> bool:
        root = self.tree
        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        return root.word

    def startsWith(self, prefix: str) -> bool:
        root = self.tree
        for w in prefix:
            if w not in root.children:
                return False
            root = root.children[w]
        return True
        
        