class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = 0
        result = deque()

        while r < len(arr) and arr[r] < x :
            r += 1

        if r == len(result)-1:
            return arr[len(arr)-k:]
        l = r - 1
        print(l)
        print(r)
        while len(result)< k:
            if l < 0:
                result.append(arr[r])
                r+= 1
            elif r >= len(arr):
                result.appendleft(arr[l])
                l -= 1
            elif x - arr[l] > arr[r] - x:
                result.append(arr[r])
                r+= 1
            else:
                result.appendleft(arr[l])
                l -= 1
        return list(result)
