class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l+r) // 2
            test_days = 1
            current = 0

            for w in weights:
                if current + w > mid:
                    test_days += 1
                    current = w
                else:
                    current += w
            if test_days > days:
                l = mid + 1
            else:
                r = mid - 1
        return l