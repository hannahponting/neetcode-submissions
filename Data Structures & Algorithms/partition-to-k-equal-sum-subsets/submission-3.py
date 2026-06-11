class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsets = [0]*k
        total = sum(nums)
        if total % k:
            return False
        count = total // k
        nums = sorted(nums, reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= count:
                    subsets[j]+= nums[i]
                    if backtrack(i+1):
                        return True
                    subsets[j]-= nums[i]
                if subsets[j] == 0:
                    break
            return False

        return backtrack(0)


