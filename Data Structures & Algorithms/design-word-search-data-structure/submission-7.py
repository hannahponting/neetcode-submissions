class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            if j == len(word):
                return root.word
            curr = word[j]
            if curr != '.':
                if curr not in root.children:
                    return False
                return dfs(j+1, root.children[curr])
            else:
                for child in root.children:
                    if dfs(j+1, root.children[child]):
                        return True
                return False
        return dfs(0, self.trie)
            
        
