class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        response = []
        deque = collections.deque()

        for j in range(len(nums)):
            if deque and deque[0] <= j-k:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[j]:
                deque.pop()
            deque.append(j)
            if j >= k -1:
                response.append(nums[deque[0]])
        return response


