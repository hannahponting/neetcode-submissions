class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtrack(i, subset):
            if subset not in ans:
                ans.append(subset[:])

            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()
                backtrack(j+1, subset)
        
        backtrack(0, [])
        return ans