class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed_count = 0

        for index, num in enumerate(nums):
            if num == val:
                removed_count += 1
            else:
                nums[index-removed_count] = num
        return len(nums)-removed_count