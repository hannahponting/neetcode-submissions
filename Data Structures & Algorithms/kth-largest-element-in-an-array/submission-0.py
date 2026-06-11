class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        values = []
        while len(values) < k:
            values.append(heapq.heappop(nums))
        return -values[-1]