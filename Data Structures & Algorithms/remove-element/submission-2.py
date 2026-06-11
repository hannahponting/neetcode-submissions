class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        for index, number in enumerate(nums):
            if number != val:
                nums[k] = number
                k += 1
        return k
