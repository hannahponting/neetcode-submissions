class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        s_to_t = defaultdict(list)
        for u, v, t in times:
            s_to_t[u].append((t, v))
    
        q = [(0, k)]

        while q:
            time, dest = heapq.heappop(q)
            if dest in seen: 
                continue
            seen.add(dest)
            if len(seen) == n:
                return time
    
            for i in s_to_t[dest]:
                if i[1] not in seen:
                    heapq.heappush(q, (time+i[0], i[1]))
        return -1
                




