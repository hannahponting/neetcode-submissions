class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suffix = [1] * (len(nums) + 1)
        response = [0] * len(nums)
        prefix = 1

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        print(suffix)

        for i in range(len(nums)):
            response[i] = suffix[i+1] * prefix
            prefix = prefix * nums[i]
            print(prefix)
        return response