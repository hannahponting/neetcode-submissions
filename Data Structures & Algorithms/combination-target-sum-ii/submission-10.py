class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        def backtracking(i, subset, total):
            if total == target:
                res.append(subset[:])
            
            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                backtracking(j+1, subset, total+candidates[j])
                subset.pop()


        backtracking(0, [], 0)
        return res