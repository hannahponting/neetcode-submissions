class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        response = []
        for i in range(len(nums)-k+1):
            j = i + k 
            window = nums[i:j]
            print(window)
            response.append(max(window))
        return response
