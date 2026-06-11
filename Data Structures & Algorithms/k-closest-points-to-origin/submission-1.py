class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            res.append((-(x*x+y*y), [x,y]))
        heapq.heapify(res)

        while len(res) > k:
            heapq.heappop(res)
        result = []
        while res:
            result.append(heapq.heappop(res)[1])
        return result
