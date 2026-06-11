class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def backtrack(i, stack, total):
            if total == target and stack not in res:
                res.append(stack[::])
            
            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                stack.append(candidates[j])
                backtrack(j+1, stack, total+candidates[j])
                stack.pop()

        backtrack(0, [], 0)
        return res