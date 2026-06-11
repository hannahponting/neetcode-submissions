class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for x in range(len(nums)):
            if nums[x] <= 0:
                j = x + 1
                k = len(nums)-1
                while j < k:
                    if (nums[x] + nums[j] + nums[k]) == 0 and [nums[x], nums[j], nums[k]] not in result:
                        result.append([nums[x], nums[j], nums[k]])
                        j += 1
                    elif (nums[x] + nums[j] + nums[k]) > 0:
                        k -= 1
                    else:
                        j += 1
        return result



