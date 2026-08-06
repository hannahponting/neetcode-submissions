class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            minLength = min(len(words[i]), len(words[i+1]))
            if len(words[i]) > len(words[i+1]) and words[i][:minLength] == words[i+1][:minLength]:
                return ""
            for j in range(minLength):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break
        
        result = []
        visited = {}
        def dfs(l):
            if l in visited:
                return visited[l]
            
            visited[l] = True

            for a in adj[l]:
                if dfs(a):
                    return True
            visited[l] = False
            result.append(l)


        for w in words:
            for l in w:
                if dfs(l):
                    return ""
        return ''.join(result[::-1])


