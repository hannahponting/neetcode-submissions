class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        # min is now l
        middle = l
        l = 0
        r = len(nums)-1

        if middle == 0:
            pass
        elif target >= nums[0]:
            r = middle -1 
        else:
            l = middle
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


        
