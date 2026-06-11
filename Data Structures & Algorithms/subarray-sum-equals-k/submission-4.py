class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0: 1}
        current = 0
        res = 0

        for num in range(len(nums)):
            current = current + nums[num]

            res += prefixes.get(current - k, 0)
            prefixes[current] = 1 + prefixes.get(current, 0)
        return res