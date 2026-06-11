class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        l = 0
        r = -1
        currentSum = 0
        minlength = 100001

        while l < len(nums) and r < len(nums):
            while currentSum < target:
                if r == len(nums)-1:
                    if minlength ==100001:
                        return 0
                    else:
                        return minlength
                r += 1
                currentSum += nums[r]
                print(f"r:{r} l:{l} current sum {currentSum}")
            minlength = min(r-l+1, minlength)
            currentSum -= nums[l]
            l += 1
        if minlength ==100001:
            return 0
        else:
            return minlength

            
