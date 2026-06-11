class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixmap =  {0: 1}
        current = 0
        res = 0

        for i in range(len(nums)):
            current += nums[i]
            diff = current - k

            res += prefixmap.get(diff, 0)
            prefixmap[current] = 1 + prefixmap.get(current, 0)

        return res
