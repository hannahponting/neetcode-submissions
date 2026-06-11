class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            current = 0
            number = 1

            for num in nums:
                if current + num > largest:
                    number += 1
                    current = num
                    if number > k:
                        return False
                else:
                    current += num
            return True
        
        l = max(nums)
        r = sum(nums)

        res = r
        while l <= r:
            mid = (l + r) // 2
            result = canSplit(mid)
            if result:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res
