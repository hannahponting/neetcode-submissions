class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        response = [False] * (len(nums) + 1)
        for num in nums:
            if num >= 1 and num <= len(nums):
                response[num] = True
        for i in range(1, len(nums)+1):
            if response[i] == False:
                return i
        return len(nums) + 1