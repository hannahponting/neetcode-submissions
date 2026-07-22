class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        res = [0]  * (len(nums))

        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        res[2] = nums[0] + nums[2]

        for j in range(3, len(nums)):
            res[j] = max(res[j-2]+ nums[j], res[j-3]+ nums[j])
        return max(res[-1], res[-2])