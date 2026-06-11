class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        before = [1]*len(nums)
        after = [1]*len(nums)
        # 0, 1, 2, 3

        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
        for i in range(len(nums)-1):
            after[len(nums)-i-2] = after[len(nums)-i-1] * nums[len(nums)-i-1]
        
        response = [0]*len(nums)
        for i in range(len(nums)):
            response[i] = before[i] * after[i]
        return response
