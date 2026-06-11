class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for i in nums:
            seen[str(i)] += 1
            if seen[str(i)] > len(nums) // 2:
                return i