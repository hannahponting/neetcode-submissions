class Solution:
    def rob(self, nums: List[int]) -> int:
        def calc(arr):
            if not arr:
                return 0
            if len(arr) <= 2:
                return max(arr)
            res = [0]  * (len(arr))

            res[0] = arr[0]
            res[1] = max(arr[0], arr[1])
            res[2] = arr[0] + arr[2]

            for j in range(3, len(arr)):
                res[j] = max(res[j-2]+ arr[j], res[j-3]+ arr[j])
            return max(res[-1], res[-2])
        if len(nums) <2:
            return max(nums)
        return max(calc(nums[1:]), calc(nums[:-1]))