class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset):
            if sum(subset) == target:
                res.append(subset[:])
                return
            
            if sum(subset) > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                subset.append(candidates[j])
                backtrack(j+1, subset)
                subset.pop()

        backtrack(0, [])
        return res