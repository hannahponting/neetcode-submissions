class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def flip(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        flip(0, len(nums)-1)
        flip(0, k%len(nums)-1)
        flip(k%len(nums), len(nums)-1)
