class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtracking(i, subset):
            if subset not in res:
                res.append(subset[:])
            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtracking(j+1, subset)
                subset.pop()
            
        backtracking(0, [])
        return res