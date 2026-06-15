class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        room = []
        count = [0]*n
        for i in range(n):
            heapq.heappush(room, (0, i))

        for start_time, end_time in meetings:
            while room and room[0][0] < start_time:
                start, num = heapq.heappop(room)
                heapq.heappush(room, (start_time, num))
            start, num = heapq.heappop(room)
            heapq.heappush(room, (start+ end_time - start_time, num))
            count[num] += 1
        return count.index(max(count))