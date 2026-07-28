class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = [[0]*2 for i in range(len(nums))]
        res[n-1][1] = res[n-1][0] = nums[n-1]

        for i in range(len(nums)-2, -1, -1):
            res[i][1] = max(nums[i], res[i+1][1] + nums[i])
            res[i][0] = max(res[i][1], res[i+1][0])
        return res[0][0]