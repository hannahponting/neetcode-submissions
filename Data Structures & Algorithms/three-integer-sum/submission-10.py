class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
        
            r = len(nums)-1
            l = i +1
            while l < r:
                total = nums[r]+ nums[l]+ nums[i]
                if total == 0:
                    result.append([nums[r], nums[l], nums[i]])
                    l += 1
                    r -=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total >0:
                    r -=1
                else:
                    l += 1
        return result
            