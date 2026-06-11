class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for index, value in enumerate(nums):
            if target-value in seen_nums:
                return [seen_nums[target-value], index]
            else:
                seen_nums[value] = index
        return []
            