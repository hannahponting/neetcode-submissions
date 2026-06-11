class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        root = self.trie
        for i in word:
            if not root.children[ord(i)-ord('a')]:
                root.children[ord(i)-ord('a')] = TrieNode()
            root = root.children[ord(i)-ord('a')]
        root.end = True

    def search(self, word: str) -> bool:
        root = self.trie
        for w in word:
            if not root.children[ord(w)-ord('a')]:
                return False
            root = root.children[ord(w)-ord('a')]
        return root.end
        
    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for w in prefix:
            if not root.children[ord(w)-ord('a')]:
                return False
            root = root.children[ord(w)-ord('a')]
        return True
        
        