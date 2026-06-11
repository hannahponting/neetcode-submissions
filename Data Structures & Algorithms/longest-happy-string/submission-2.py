class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = []
        if a:
            letters.append((-a, "a"))
        if b:
            letters.append((-b, "b"))
        if c:
            letters.append((-c, "c"))
        heapq.heapify(letters)
        res = []

        while letters:
            print(res, letters)
            l = heapq.heappop(letters)
            if len(res) >= 2 and l[1] == res[-1] and l[1] == res[-2]:
                if letters:
                    second = heapq.heappop(letters)
                else:
                    return "".join(res)
                heapq.heappush(letters, l)
                l = second
            res.append(l[1])
            if l[0] < -1:
                heapq.heappush(letters, (l[0]+1, l[1]))
        return "".join(res)
