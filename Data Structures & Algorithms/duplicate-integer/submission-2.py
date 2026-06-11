class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integers_appeared ={}
        for i in nums:
            if integers_appeared.get(str(i)):
                return True
            else:
                integers_appeared[str(i)] = True
        return False