class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_nums = set(nums)
        max_sequence = 0
        sequence = 0

        for i in range(len(nums)):
            if nums[i]-1 not in seen_nums:
                current = nums[i]
                while current in seen_nums:
                    sequence += 1
                    max_sequence = max(max_sequence, sequence)
                    current += 1
                sequence = 0
        return max_sequence