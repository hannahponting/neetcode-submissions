class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared = {}
        for index in range(len(nums)):
            if target-nums[index] in appeared:
                return [appeared[target-nums[index]], index]
            appeared[nums[index]] = index