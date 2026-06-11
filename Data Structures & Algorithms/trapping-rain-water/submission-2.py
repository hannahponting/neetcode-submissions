class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]* len(height)
        right_max = [0]*len(height)

        left_max_value = 0
        right_max_value = 0
        for i in range(len(height)):
            left_max_value = max(left_max_value, height[i])
            left_max[i] = left_max_value
        
        for i in range(len(height)-1, -1, -1):
            right_max_value = max(right_max_value, height[i])
            right_max[i] = right_max_value
        print(left_max)
        print(right_max)

        water = 0
        for i in range(len(height)):
            if (min(left_max[i], right_max[i])-height[i]) > 0:
                water = water +min(left_max[i], right_max[i])-height[i]
        return water