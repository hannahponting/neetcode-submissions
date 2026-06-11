class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            nonlocal res
            sub = []

            for n in subset:
                sub.append(n)
            res.append(sub)

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()

        backtrack(0, [])
        return res
