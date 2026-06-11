class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        max_sequence = 1

        for i in nums:
            sequence = 1
            if (i-1) not in set_nums:
                count = 0
                while True:
                    if i+count in set_nums:
                        count = count +1
                        max_sequence = max(max_sequence, count)
                    else:
                        break
        return max_sequence

                

        