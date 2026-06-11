class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for index, value in enumerate(nums):
            if value == val:
                k += 1
            else:
                nums[index - k] = value
        return len(nums) - k