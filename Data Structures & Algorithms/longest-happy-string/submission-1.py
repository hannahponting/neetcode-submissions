class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = []

        for letter, count in [('a', -a), ('b',-b), ('c',-c)]:
            if count != 0:
                heapq.heappush(heap, (count, letter))

        while heap:
            count1, letter1 = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == letter1:
                if heap:
                    count2, letter2 = heapq.heappop(heap)
                    res.append(letter2)
                    count2 += 1
                    if count2 != 0:
                        heapq.heappush(heap, (count2, letter2))
                else:
                    return ''.join(res)
            res.append(letter1)
            count1 += 1
            if count1 != 0:
                heapq.heappush(heap, (count1, letter1))
        return ''.join(res)