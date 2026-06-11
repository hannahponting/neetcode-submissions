class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, seen):
            if len(subset) == len(nums):
                res.append(subset[::])
                return
            
            for j in range(len(nums)):
                if seen[j]:
                    continue
                subset.append(nums[j])
                seen[j] = True
                backtrack(subset, seen)
                subset.pop()
                seen[j] = False

        backtrack([], [False]*len(nums))
        return res