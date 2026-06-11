class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(maxW):
            current_days = 1
            weight = 0
            for w in weights:
                if weight + w > maxW:
                    current_days += 1
                    weight = w
                    if current_days > days:
                        return False
                else:
                    weight += w
            return True
        
        l = max(weights)
        r = sum(weights)
        result = 0
        while l <= r:
            mid = (l+r)//2
            res = canShip(mid)
            if res:
                result = mid
                r = mid -1
            else:
                l = mid + 1
        
        return result