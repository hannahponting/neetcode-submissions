class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_nums = 0
        max_int = 0
        appearences = defaultdict(int)
        for num in nums:
            appearences[str(num)] += 1
            if appearences[str(num)] > max_nums:
                max_nums = appearences[str(num)]
                max_int = num
        return max_int