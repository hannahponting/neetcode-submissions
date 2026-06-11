class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        counts = [-c for c in counts.values()]
        heapq.heapify(counts)
        queue = []
        heapq.heapify(queue)
        time = 0
        print(counts)
        print(queue)

        while counts or queue:
            time += 1
            if queue and time >= queue[0][0]:
                time, task = heapq.heappop(queue)
                heapq.heappush(counts, task)
            
            if counts:
                num = heapq.heappop(counts)
                if num < -1:
                    heapq.heappush(queue, (time + n+1, num + 1))
        return time
