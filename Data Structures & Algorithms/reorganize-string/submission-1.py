class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = [(-freq, ch) for ch, freq in Counter(s).items()]
        heapq.heapify(counts)

        result = []
        hold = None

        while counts:
            times, ch = heapq.heappop(counts)

            # if same as last char, try next option
            if result and result[-1] == ch:
                if not counts:
                    return ""  # no alternative → impossible
                times2, ch2 = heapq.heappop(counts)
                result.append(ch2)

                if times2 < -1:
                    heapq.heappush(counts, (times2 + 1, ch2))

                heapq.heappush(counts, (times, ch))  # put original back
            else:
                result.append(ch)
                if times < -1:
                    heapq.heappush(counts, (times + 1, ch))

        return ''.join(result)
