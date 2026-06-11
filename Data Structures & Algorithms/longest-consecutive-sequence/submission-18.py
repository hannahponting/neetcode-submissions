class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(list(set(nums)))
        max_sequence = 1
        i = 0
        sequence = 1

        while i < len(nums)-1:
            print(nums[i])
            print(nums[i+1])
            if nums[i]+1 == nums[i+1]:
                sequence += 1
                max_sequence = max(max_sequence, sequence)
            else:
                sequence = 1
            i +=1
        return max_sequence