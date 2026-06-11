class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        current = []
        cCap = capacity
        distance = 0

        for trip in trips:
            heapq.heappush(heap, (trip[1], trip[2], trip[0])) # (start, end, people)
        while heap:
            if not current:
                distance = heap[0][0]
            else:
                distance = min(heap[0][0], current[0][0])
            while current and current[0][0] <= distance:
                removed = heapq.heappop(current)
                cCap += removed[1]
            if heap and heap[0][0] <= distance:
                trip1 = heapq.heappop(heap)
                cCap -= trip1[2]
                if cCap < 0:
                    return False
                else:
                    heapq.heappush(current, (trip1[1], trip1[2])) 
        return True

            
            
