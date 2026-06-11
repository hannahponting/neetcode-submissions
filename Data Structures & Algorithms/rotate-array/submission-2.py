class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = []
        for num in nums:
            copy.append(num)
            
        for i in range(len(nums)):
            if i + k > len(nums)-1:
                index = i+k
                while index > len(nums)-1:
                    index -= len(nums)
                nums[index] = copy[i]
            else:
                print(f'i: {i} -> {i + k}')
                nums[i+k] = copy[i]