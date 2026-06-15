"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        res = 0

        for i in range(len(intervals)):
            time.append((intervals[i].start, 1))
            time.append((intervals[i].end, -1))

        time.sort(key = lambda t: (t[0], t[1]))

        current = 0
        for i in time:
            current += i[1]
            res = max(res, current)
        return res
