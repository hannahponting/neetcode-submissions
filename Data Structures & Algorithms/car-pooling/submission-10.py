class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = []
        for t in trips:
            heapq.heappush(sorted_trips, (t[1], t[2], t[0])) # (from, to, num)
        distance = 0
        car = [] 
        total = 0
        while sorted_trips:
            distance = sorted_trips[0][0]
            while car and distance >= car[0][0]:
                leaving = heapq.heappop(car)
                total -= leaving[1]
            trip = heapq.heappop(sorted_trips)
            if trip[2] + total > capacity:
                return False
            else: 
                total += trip[2]
                heapq.heappush(car, (trip[1], trip[2]))
        return True
