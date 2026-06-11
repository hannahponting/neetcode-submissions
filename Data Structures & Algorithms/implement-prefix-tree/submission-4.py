class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.trie
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
        