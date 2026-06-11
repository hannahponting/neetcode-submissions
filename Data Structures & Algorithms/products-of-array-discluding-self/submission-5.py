class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffexes = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffexes[i] = suffexes[i+1] * nums[i+1]
        
        prefixes = 1
        for i in range(len(nums)):
            result[i] = prefixes * suffexes[i]
            prefixes = prefixes * nums[i]
        return result

