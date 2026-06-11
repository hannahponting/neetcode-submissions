class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        response = []
        deque = collections.deque()
        i = r = 0
        while r < len(nums):
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)

            if i > deque[0]:
                deque.popleft()
            
            if (r+1) >= k:
                response.append(nums[deque[0]])
                i += 1
            r +=1
        return response
