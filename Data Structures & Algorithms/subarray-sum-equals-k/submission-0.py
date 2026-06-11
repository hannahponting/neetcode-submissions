class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = currentSum = 0
        prefixes = {0: 1}

        for num in nums:
            currentSum += num
            result += prefixes.get(currentSum - k, 0)
            prefixes[currentSum] = prefixes.get(currentSum, 0) + 1
        return result