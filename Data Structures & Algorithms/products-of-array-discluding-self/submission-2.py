class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        response = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            response[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            response[i] *= postfix
            postfix *= nums[i]
        return response
        
