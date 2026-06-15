"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.end)
        if not intervals:
            return True
        prevEnd = intervals[0].start

        for i in range(len(intervals)):
            if intervals[i].start < prevEnd:
                return False
            else:
                prevEnd = intervals[i].end
        return True