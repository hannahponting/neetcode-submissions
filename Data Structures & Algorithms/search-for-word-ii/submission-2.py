class Trie:
    def __init__(self):
        self.children = {}
        self.word = False
        self.full = ""


class Tries:
    def __init__(self):
        self.tree = Trie()

    def build(self, word):
        curr = self.tree

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]

        curr.word = True
        curr.full = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Tries()

        for word in words:
            tree.build(word)

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, curr):
            # bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            ch = board[r][c]

            # visited or invalid trie path
            if ch == "#" or ch not in curr.children:
                return

            node = curr.children[ch]

            # found a word
            if node.word:
                res.append(node.full)
                node.word = False  # avoid duplicates

            # mark visited
            board[r][c] = "#"

            # explore neighbors
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # backtrack
            board[r][c] = ch

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, tree.tree)

        return res