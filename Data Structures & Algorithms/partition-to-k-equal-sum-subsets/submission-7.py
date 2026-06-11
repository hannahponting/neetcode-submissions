class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        side = total // k

        if total % k != 0:
            return False
        if nums[0] > side:
            return False
        
        sides = [0] * k

        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if sides[j] + nums[i] <= side:
                    sides[j] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= nums[i]
                if sides[j] == 0:
                    break
                
            return False

        return dfs(0)