class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for num in nums:
            if candidate2 != num and count1 == 0:
                candidate1 = num
            elif candidate1 != num and count2 == 0:
                candidate2 = num
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)
        return result