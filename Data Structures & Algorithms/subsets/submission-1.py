class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        def backtrack(i, stack):
            res.append(stack[::])

            for j in range(i, len(nums)):
                stack.append(nums[j])
                backtrack(j+1, stack)
                stack.pop()
        
        backtrack(0, [])
        return res