class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, stack):
            nonlocal res
            total = 0
            for num in stack:
                total ^= num
            res += total

            for j in range(i, len(nums)):
                stack.append(nums[j])
                backtrack(j+1, stack)
                stack.pop()

        backtrack(0, [])
        return res