class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        response = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    print(nums[i]+nums[j]+nums[k])
                    if nums[i]+nums[j]+nums[k] == 0:
                        sorted_nums = sorted([nums[i],nums[j],nums[k]])
                        if sorted_nums not in response:
                          response.append(sorted_nums)
        return response

        