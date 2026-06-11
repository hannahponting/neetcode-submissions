class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0] * (len(height)+1)
        maxr = [0] * (len(height)+1)

        for i in range(len(maxr)-2, -1, -1):
            maxr[i] = max(height[i], maxr[i+1])

        rain = 0
        print(maxl)
        
        for i in range(len(height)):
            maxl[i+1] = max(height[i], maxl[i])
            water = min(maxl[i], maxr[i]) - height[i]
            if water > 0:
                rain += water
        return rain
