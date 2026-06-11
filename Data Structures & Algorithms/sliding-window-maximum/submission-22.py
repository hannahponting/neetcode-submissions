class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * len(nums)
        d = deque() # decreasing queue

        for i in range(len(nums)):
            while d and nums[i] > d[-1][0]:
                d.pop()
            d.append((nums[i], i))
            if d[0][1] <= i-k:
                d.popleft()
            res[i]= d[0][0]
        return res[k-1:]
            

