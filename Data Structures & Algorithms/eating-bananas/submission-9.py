class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatInHours(rate):
            hours = 0
            for p in piles:
                hours += math.ceil(p/rate)
                if hours > h:
                    return False
            return True
        
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            mid = (l+r) // 2
            result = canEatInHours(mid)
            if result:
                res = mid
                r = mid -1 
            else:
                l = mid + 1
        return res

