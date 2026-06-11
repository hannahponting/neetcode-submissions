class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        result = r

        while l <= r:
            mid = (l + r) // 2

            total = 0
            packages = []
            for package in weights:
                if total + package <= mid:
                    total += package
                else:
                    packages.append(total)
                    total = package
            packages.append(total)

            if len(packages) <= days:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result
