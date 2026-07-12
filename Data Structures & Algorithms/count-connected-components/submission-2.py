class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def findParent(n1):
            res = parents[n1]
            while res != parents[res]:
                parents[n1] = parents[parents[n1]]
                res = parents[n1]
            return res
        
        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parents[p2] = p1
            else:
                rank[p2] += rank[p1]
                parents[p1] = p2
            return 1

        res = n
        for l, r in edges:
            res -= union(l,r)
        return res
