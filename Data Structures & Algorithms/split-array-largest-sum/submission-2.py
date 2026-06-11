class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_num):
            count = 1
            current = 0
            for num in nums:
                if current + num > max_num:
                    count +=1
                    current = num
                else:
                    current += num
                if count > k:
                    return False
            return True

        l = max(nums)
        r = sum(nums)
        
        res = r
        while l <= r:
            mid = (l+r) // 2
            if canSplit(mid):
                r = mid -1
                res = mid
            else: 
                l = mid +1
        return res
