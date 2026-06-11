class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def backtracking(i, subset, total):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            
            if total > target:
                return

            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                backtracking(j+1, subset, total+nums[j])
                subset.pop()

        backtracking(0, [], 0)
        return res
