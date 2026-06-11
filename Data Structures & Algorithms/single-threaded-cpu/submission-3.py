class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waiting = []
        heapq.heapify(waiting)
        ready = []
        heapq.heapify(ready)

        i = 0
        for t in tasks:
            heapq.heappush(waiting , (t[0], t[1], i))
            i += 1
        

        res = []
        self.time = 0
        while waiting or ready:
            while waiting and waiting[0][0] <= self.time:
                task = heapq.heappop(waiting)
                heapq.heappush(ready, (task[1], task[2]))
            
            if ready:
                process = heapq.heappop(ready)
                self.time += process[0]
                res.append(process[1])

            else:
                self.time = waiting[0][0]
        return res