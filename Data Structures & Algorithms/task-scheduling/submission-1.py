class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        q = deque()
        counts = [-v for v in counts.values()]
        heapq.heapify(counts)

        print(counts)
        time = 0
        while counts or q:
            time += 1
            if counts:
                count = heapq.heappop(counts)
                count += 1
                if count < 0:
                    q.append((count, time+n))
            while q and q[0][1] <= time:
                heapq.heappush(counts, q.popleft()[0])
            print(counts)
            print(q)
        return time

