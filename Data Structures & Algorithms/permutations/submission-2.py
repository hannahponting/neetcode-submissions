class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def backtrack( subset, seen):
            if len(subset) == len(nums):
                res.append(subset[:])
            
            for j in range(len(nums)):
                if not seen[j]:
                    subset.append(nums[j])
                    seen[j] = True
                    backtrack(subset, seen)
                    seen[j] = False
                    subset.pop()
        
        backtrack([], [False]*len(nums))
        return res