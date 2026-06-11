class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
                if count >= len(nums)//2:
                    return candidate
            else:
                count -= 1
            
        return candidate
