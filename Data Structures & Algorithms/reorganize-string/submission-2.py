class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        res = []
        heapq.heapify(res)

        for c in counts:
            heapq.heappush(res, (-counts[c], c))
        
        result = []
        carry = None

        while res or carry:
            if res:
                letter = heapq.heappop(res)
                if result and letter[1] == result[-1]:
                    return ''
                result.append(letter[1])
            if carry:
                heapq.heappush(res, carry)
                carry = None
            if letter and letter[0] < -1:
                carry = (letter[0]+1, letter[1])
            letter = None
        return ''.join(result)
        
