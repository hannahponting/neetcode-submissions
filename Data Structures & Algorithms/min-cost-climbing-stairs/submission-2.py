class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def calculate(arr):
            if len(arr) < 3:
                return min(arr)
            res = [0] * (len(arr)+1)
            res[0] = arr[0]
            res[1] = arr[0] + arr[1]
            
            for j in range(2, len(arr)):
                res[j] = min(res[j-1]+arr[j], res[j-2]+arr[j])
            res[-1] = min(res[-2], res[-3])
            return res[-1]

        return min(calculate(cost), calculate(cost[1:]))