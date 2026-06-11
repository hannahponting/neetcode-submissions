class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_seen = {}

        for index, value in enumerate(numbers):
            if nums_seen and target-value in nums_seen:
                return [nums_seen[target-value]+1, index+1]
            else:
                nums_seen[value] = index
        return []