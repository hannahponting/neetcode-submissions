class Solution:
    def trap(self, height: List[int]) -> int:
        highestleft = [0]*len(height)
        highestright = [0]*len(height)
        total = 0

        for i in range(1, len(height)):
            highestleft[i] = max(highestleft[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            highestright[i] = max(highestright[i+1], height[i+1])

        for i in range(len(height)):
            water = min(highestleft[i], highestright[i]) - height[i]      
            if water > 0:
                total += water 
                print(water) 
        return total