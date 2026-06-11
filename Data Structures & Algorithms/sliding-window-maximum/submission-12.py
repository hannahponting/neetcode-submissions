class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        response = [0]*(len(nums)-k+1)
        for i in range(len(nums)-k+1):
            maximum = nums[i]
            if i+k > len(nums):
                break
            else:
                for j in range(i, i+k):
                    maximum = max(maximum, nums[j])
            response[i] = maximum
        return response