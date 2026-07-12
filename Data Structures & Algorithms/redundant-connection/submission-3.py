class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def parent(n1):
            if n1 != parents[n1]:
                parents[n1] = parent(parents[n1])
            return parents[n1]
        
        def union(n1, n2):
            p1, p2 = parent(n1), parent(n2)
            
            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]
                parents[p1] = p2
            else:
                rank[p1] += rank[p2]
                parents[p2] = p1
            return True
        
        for l, r in edges:
            if not union(l, r):
                return [l, r]