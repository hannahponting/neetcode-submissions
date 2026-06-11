class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        result = []

        for i in range(len(nums)):
            while que and que[-1][0] < nums[i]:
                que.pop()
            que.append((nums[i], i))
            while que and que[0][1] <= i-k:
                que.popleft()
            if i >= k-1:
                result.append(que[0][0])
        return result