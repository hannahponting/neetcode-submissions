"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda l:l.start)
        taken = []
        number = 0

        for i in range(len(intervals)):
            while taken and taken[0] <= intervals[i].start:
                heapq.heappop(taken)
            heapq.heappush(taken, intervals[i].end)
            number = max(number, len(taken))
        return number
