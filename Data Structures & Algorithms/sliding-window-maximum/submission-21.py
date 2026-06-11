class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() 
        result = []

        for i in range(len(nums)):
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append((nums[i], i))
            if dq and dq[0][1] <= i-k:
                dq.popleft()
            if i >= k-1:
                result.append(dq[0][0])
        return result


        
