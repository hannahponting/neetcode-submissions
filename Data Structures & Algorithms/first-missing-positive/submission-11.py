class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present = [False] * (len(nums)+1)

        for num in nums:
            if num > 0 and num < len(nums)+1:
                present[num-1] = True

        for num in range(1, len(nums)+2):
            if not present[num-1]:
                return num