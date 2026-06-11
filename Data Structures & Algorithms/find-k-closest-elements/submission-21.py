class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()

        r = 0
        while r != len(arr) and arr[r] < x:
            r += 1
        
        if r ==len(arr):
            return arr[-k:]

        l = r - 1

        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1
            
            elif r >= len(arr):
                res.appendleft(arr[l])
                l -= 1

            elif  (arr[r] - x) == (x-arr[l]) or (arr[r] - x) > (x-arr[l]):
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return list(res)
        


