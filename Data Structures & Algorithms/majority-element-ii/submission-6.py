class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif candidate1 == None or count1 == 0:
                candidate1 = nums[i]
                count1 += 1
            elif candidate2 == None or count2 == 0:
                candidate2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        response = []
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        if count1 > len(nums)/3:
            response.append(candidate1)
        if count2 > len(nums)/3:
            response.append(candidate2)
        

        return response
        