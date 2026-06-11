class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = deque() # (-count, time)

        while maxHeap or queue:
            time += 1
            if not maxHeap:
                time = queue[0][1]
            else:
                num = heapq.heappop(maxHeap)
                num += 1
                if num < 0:
                    queue.append((num, time+n))
            if queue and queue[0][1] <= time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time


