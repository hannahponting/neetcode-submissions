class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currentSum = 0
        minlength = float('inf')

        for r in range(len(nums)):
            currentSum += nums[r]

            while currentSum >= target:
                minlength = min(r-l+1, minlength)
                currentSum -= nums[l]
                l += 1
                
        if minlength == float('inf'):
            return 0
        else:
            return minlength

            
