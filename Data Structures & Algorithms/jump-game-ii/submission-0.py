class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        count = 0
        while r < len(nums)-1:
            farthest = 1
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            count += 1
        return count
