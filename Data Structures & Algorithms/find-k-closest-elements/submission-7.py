class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = 0
        result = deque()

        while r < len(arr) and arr[r] < x:
            r += 1
        l = r-1
        while len(result) < k:
            if l < 0:
                result.append(arr[r])
                r += 1
            elif r >= len(arr):
                result.appendleft(arr[l])
                l -= 1
            elif x - arr[l] == arr[r] - x or x - arr[l] < arr[r] - x:
                result.appendleft(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
            
        return list(result)
                
        
        