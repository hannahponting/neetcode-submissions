class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[index-k] = nums[index]
            else:
                k += 1
        return len(nums)-k