class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for key in counts:
            buckets[counts[key]].append(key)

        res = []
        for i in range(len(buckets)-1, -1,-1):
            for value in buckets[i]:
                res.append(value)
                if len(res)== k:
                    return res
