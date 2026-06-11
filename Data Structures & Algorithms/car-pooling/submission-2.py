class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        li = []
        heapq.heapify(li)
        distance = 0
        current = []
        heapq.heapify(current)
        capacity


        for num, start, end in trips:
            heapq.heappush(li, (start, end, num))
        
        while current or li: 
            if current and li:
                distance = min(current[0][0], li[0][0])
            elif current:
                distance = current[0][0]
            else:
                distance = li[0][0]
            if current and distance == current[0][0]:
                leave = heapq.heappop(current)
                capacity += leave[1]
            if li and distance == li[0][0]:
                s1, e1, n1 = heapq.heappop(li)
                heapq.heappush(current, (e1, n1))
                capacity -= n1
                if capacity < 0:
                    return False
            distance += 1
        return True


