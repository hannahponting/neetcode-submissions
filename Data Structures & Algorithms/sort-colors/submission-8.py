class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        b = len(nums)-1
        i = 0

        while i <= b:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[r] = nums[r], nums[i]
                i += 1
                r += 1
            else:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
