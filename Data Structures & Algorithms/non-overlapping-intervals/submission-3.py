class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key = lambda pair: pair[1])
        count = 0

        for i in range(len(intervals)):
            if not res or res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            else:
                count += 1
        return count