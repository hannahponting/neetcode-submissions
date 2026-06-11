class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones] 
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 > stone2:
                heapq.heappush(stones, stone2-stone1)
            if stone1 < stone2:
                heapq.heappush(stones, stone1-stone2)
        if stones:
            return - stones[0]
        return 0
        