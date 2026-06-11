class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minLength = float('inf')
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                l += 1
                minLength = min(minLength, r - l + 2)
        if minLength == float('inf'):
            return 0
        return minLength


