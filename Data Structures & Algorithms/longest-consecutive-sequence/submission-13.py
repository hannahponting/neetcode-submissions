class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_numbers = set(nums)
        maximum = 0
        for i in nums:
            if i-1 not in seen_numbers:
                length = 1
                while (i + length) in seen_numbers:
                    length = length + 1
                maximum = max(length, maximum)
        return maximum



