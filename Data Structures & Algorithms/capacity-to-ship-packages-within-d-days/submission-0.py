class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canShip(cap):
            ships = 1
            current_weight = 0
            for w in weights:
                if w + current_weight > cap:
                    ships += 1
                    current_weight = w
                else:
                    current_weight += w
                if ships > days:
                    return False
            return True

        res = float('inf')
        while l <= r:
            pointer = (l + r) // 2
            if canShip(pointer):
                r = pointer - 1
                res = min(res, pointer)
            else:
                l = pointer + 1
        return res

    
    
    
