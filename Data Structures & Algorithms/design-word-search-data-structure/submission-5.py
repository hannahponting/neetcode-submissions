class Tries:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.tree = Tries()

    def addWord(self, word: str) -> None:
        curr = self.tree
        for w in word:
            if w not in curr.children:
                curr.children[w] = Tries()
            curr = curr.children[w]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(i, tree):
            if i == len(word):
                if tree.word:
                    return True
                else:
                    return False
            
            if word[i] != '.':
                if word[i] not in tree.children:
                    return False
                else:
                    return dfs(i+1, tree.children[word[i]])
            else:
                for child in tree.children:
                    if dfs(i+1, tree.children[child]):
                        return True
                return False
            
        return dfs(0, self.tree)
