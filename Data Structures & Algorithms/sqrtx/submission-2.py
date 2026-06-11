class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            pointer = (l + r) // 2
            square = pointer * pointer
            if square == x:
                return pointer
            if square > x:
                r = pointer -1
            else:
                l = pointer + 1
        return r
