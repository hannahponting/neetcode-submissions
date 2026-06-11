class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for index, count in counts.items():
            buckets[count].append(index)

        result = []
        for i in range(len(nums), -1, -1):
            print(i, buckets[i])
            for number in buckets[i]:
                result.append(number)
                if len(result) == k:
                    return result
        return result
