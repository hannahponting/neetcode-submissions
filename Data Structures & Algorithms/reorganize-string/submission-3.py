class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        letters = []
        for c in counts:
            heapq.heappush(letters, (-counts[c], c))
        
        res = []

        while letters:
            first = heapq.heappop(letters)
            if res and first[1] == res[-1]:
                if not letters:
                    return ""
                second = heapq.heappop(letters)
                heapq.heappush(letters, first)
                first = second
            res.append(first[1])
            if first[0] < -1:
                heapq.heappush(letters, (first[0]+1, first[1]))
        
        return "".join(res)