class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for index in range(len(nums)):
            if count == 0:
                candidate = nums[index]
                count += 1
            elif candidate == nums[index]:
                count+=1
            else:
                count -= 1
                
        return candidate
