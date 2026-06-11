class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        length = mountainArr.length()
        r = length - 1

        start = mountainArr.get(0)
        end = mountainArr.get(length-1)

        while True:
            mid = (l+r) // 2
            before = mountainArr.get(mid-1)
            val = mountainArr.get(mid)
            after = mountainArr.get(mid+1)

            if before < val > after:
                peak = mid
                break
            elif val > before:
                l = mid + 1
            else:
                r = mid - 1
        
        # search left
        peak = mid
        l = 0
        r = peak

        while l <= r:
            mid = (l+r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                r = mid -1
            else:
                l = mid + 1
        
        l = peak
        r = length
        while l <= r:
            mid = (l+r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                r = mid -1
            else:
                l = mid + 1
        
        return -1
        

