class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) == 1:
                return nums

            mid = len(nums) //2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            l = 0
            r = 0
            result = []

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            
            while l < len(left):
                result.append(left[l])
                l += 1
            while r < len(right):
                result.append(right[r])
                r += 1
            return result
            
        return mergeSort(nums)
            



