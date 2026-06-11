class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in result:
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return result