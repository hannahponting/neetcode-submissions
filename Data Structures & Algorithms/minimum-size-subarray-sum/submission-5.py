class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimumlength = float('inf')
        l = 0
        currentsum = 0

        for r in range(len(nums)):
            currentsum += nums[r]
            while target <= currentsum:
                minimumlength = min(minimumlength, r-l+1)
                currentsum -= nums[l]
                l += 1
        
        if minimumlength == float('inf'):
            return 0
        return minimumlength
            
