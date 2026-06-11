class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if count[i] > len(nums) /3 and i not in result:
                result.append(i)
        return result