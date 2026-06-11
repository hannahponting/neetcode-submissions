class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0] * (len(height))
        maxright = [0] * (len(height))
        total_water = 0

        for i in range(len(height)):
            if i == 0:
                maxleft[i] = height[i]
            else:
                maxleft[i] = max(maxleft[i-1], height[i])
        
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                maxright[i] = height[i]
            else:
                maxright[i] = max(maxright[i+1], height[i])
        print(maxleft)
        print(maxright)
        for i in range(len(height)):
            current = min(maxright[i], maxleft[i])- height[i]
            print(current)
            if current > 0:
                total_water += current
        return total_water
