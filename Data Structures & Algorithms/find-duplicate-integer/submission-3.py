class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] != i + 1:
                correct = nums[i] - 1
                
                if nums[i] == nums[correct]:
                    return nums[i]
                
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1