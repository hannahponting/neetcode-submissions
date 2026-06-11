class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = []
        res = []
        heapq.heapify(counts)
        for letter, count in [('a', a), ('b', b), ('c', c)]:
            if count > 0:
                heapq.heappush(counts, (-count, letter))

        while counts:
            c1, l1 = heapq.heappop(counts)
            if len(res) > 1 and res[-1] == res[-2] == l1:
                if not counts:
                    break
                c2, l2 = heapq.heappop(counts)
                res.append(l2)
                c2 += 1
                if c2 < 0:
                    heapq.heappush(counts, (c2, l2))    
            else:
                res.append(l1)
                c1 += 1
            if c1 < 0:
                heapq.heappush(counts, (c1, l1))
        return ''.join(res)