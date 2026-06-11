class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        highest_streak = 0
        for i in range(0, len(nums)):
            current_value = nums[i]
            streak = 1
            for j in range(i+1, len(nums)):
                if (current_value + 1 == nums[j]):
                    streak = streak + 1
                    current_value = nums[j]
                else:
                    break
            if streak > highest_streak:
                highest_streak = streak
        return highest_streak
