class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        response = []
        deque = collections.deque()
        for i in range(k):
            if deque:
                while deque and nums[deque[-1]] < nums[i]:
                    deque.pop()
            deque.append(i)
        response.append(nums[deque[0]])
        print(response)
        print(deque)
        i = 0
        for j in range(k, len(nums)):
            i += 1
            if deque[0] < i:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[j]:
                deque.pop()
            deque.append(j)
            response.append(nums[deque[0]])
            print(deque)
        return response


