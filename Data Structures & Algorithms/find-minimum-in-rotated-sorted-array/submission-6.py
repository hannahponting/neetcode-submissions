class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            pointer = (l + r) // 2
            if nums[pointer] > nums[r]:
                l = pointer + 1
            else:
                r = pointer 
        return nums[l]