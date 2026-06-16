class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                if res[-1][1] < intervals[i][0]:
                    res.append(intervals[i])
                elif res[-1][1] < intervals[i][1]:
                    res[-1][1] = intervals[i][1]
        return res