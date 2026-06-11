class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def backtrack(i, subset, total):
            if total > target:
                return
            
            if total == target:
                res.append(subset[::])
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                backtrack(j+1, subset, total + candidates[j])
                subset.pop()

        backtrack(0, [], 0)
        return res