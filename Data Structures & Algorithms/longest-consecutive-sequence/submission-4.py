class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        max_num = 0

        for i in nums:
            if i-1 not in set_of_nums:
                sequence_count = 1
                sequence_value = i+1
                while sequence_value in set_of_nums:
                    sequence_count += 1
                    sequence_value += 1
                max_num = max(max_num, sequence_count) 
        return max_num