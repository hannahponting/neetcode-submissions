class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        maximum = max(nums)
        minimum = min(nums)

        index = 0
        for i in range(minimum, maximum+1):
            while count[i] > 0:
                nums[index] = i
                count[i] -= 1
                index += 1
        return nums