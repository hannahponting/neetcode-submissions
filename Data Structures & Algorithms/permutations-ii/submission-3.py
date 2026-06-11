class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def backtrack(subset, seen):
            if len(subset) == len(nums):
                if subset not in res:
                    res.append(subset[::])
                return
            
            for j in range(len(nums)):
                if seen[j]:
                    continue
                if j > 0 and nums[j] == nums[j - 1] and not seen[j - 1]:
                    continue
                subset.append(nums[j])
                seen[j] = True
                backtrack(subset, seen)
                subset.pop()
                seen[j] = False

        backtrack([], [False]*len(nums))
        return res