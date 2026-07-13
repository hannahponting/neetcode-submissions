class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                adj_list[pattern].append(w)
        
        count = 1
        q = deque([beginWord])
        visited = set()
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for w in range(len(word)):
                    pattern = word[:w] + "*" + word[w+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            count += 1
        return 0
