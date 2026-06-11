class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []


        def backtracking(i, subset, total):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            
            if total > target:
                return

            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtracking(j, subset, total+nums[j])
                subset.pop()
        

        backtracking(0, [], 0)
        return res
