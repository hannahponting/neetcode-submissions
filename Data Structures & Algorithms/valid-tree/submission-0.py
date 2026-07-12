class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjMap = {i: [] for i in range(n)}

        for i, j in edges:
            adjMap[i].append(j)
            adjMap[j].append(i)
        
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for adj in adjMap[node]:
                if adj != prev:
                    if not dfs(adj, node):
                        return False
            return True

        return dfs(0, -1) and n == len(visit)