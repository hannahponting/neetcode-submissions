class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k=0
        while i < len(nums):
            if i > 0 and nums[i-1] == nums[i]:
                k += 1
            else:
                nums[i-k] = nums[i]
            i += 1
        return len(nums)-k