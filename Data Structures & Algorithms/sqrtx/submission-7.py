class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = l + (r-l)//2
            result = mid * mid
            if result == x:
                return mid
            elif result > x:
                r = mid-1
            else:
                l = mid + 1
        return r