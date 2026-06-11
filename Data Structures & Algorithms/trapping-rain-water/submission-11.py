class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxL = [0] * (len(height)+1)
        maxR = [0] * (len(height)+1)
        res = 0

        for i in range(len(height)-1, 0, -1):
            maxR[i-1] = max(maxR[i], height[i])
        
        for i in range(len(height)):
            maxL[i+1] = max(maxL[i], height[i])
            water = min(maxL[i], maxR[i])-height[i]
            if water > 0:
                res += water
        return res
