class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        response = [False] * (len(nums) + 1)
        for num in nums:
            if num > 0 and num <= len(nums)+1:
                response[num-1] = True
        print(response)
        for i in range(len(nums)+1):
            if response[i] == False:
                return i+1