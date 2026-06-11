class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0

        for num in num_set:
            if num - 1 not in num_set:
                number = num
                sequence = 0
                while number in num_set:
                    sequence += 1
                    number += 1
                max_sequence = max(max_sequence, sequence)
        return max_sequence