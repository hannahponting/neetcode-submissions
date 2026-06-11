class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waiting = []
        heapq.heapify(waiting)
        ready = []
        heapq.heapify(ready)
        time = 0

        index = 0
        for available, processing in tasks:
            heapq.heappush(waiting, (available, processing, index))
            index += 1

        result = []
        while waiting or ready:
            while waiting and waiting[0][0] <= time:
                task = heapq.heappop(waiting)
                heapq.heappush(ready, (task[1], task[2]))
            if not ready:
                time = waiting[0][0]
                continue
            task = heapq.heappop(ready)
            result.append(task[1])
            time += task[0]
        return result

            