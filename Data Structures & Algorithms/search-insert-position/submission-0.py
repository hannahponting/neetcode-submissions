class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            pointer = ( l + r ) // 2
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] < target:
                l = pointer + 1
            else:
                r = pointer - 1
        return l