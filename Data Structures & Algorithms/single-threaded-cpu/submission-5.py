class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        res = []
        waiting = []
        count = 0
        for t in tasks:
            waiting.append((t[0], t[1], count))
            count += 1
        heapq.heapify(waiting)

        ready = []
        
        while waiting or ready:
            if not ready and time < waiting[0][0]:
                time = waiting[0][0]
            
            while waiting and time >= waiting[0][0]:
                task = heapq.heappop(waiting)
                heapq.heappush(ready, (task[1], task[2]))
            
            if ready:
                current = heapq.heappop(ready)
                time += current[0]
                res.append(current[1])
        
        return res
