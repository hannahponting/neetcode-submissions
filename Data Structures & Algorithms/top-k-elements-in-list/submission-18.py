class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        response = []

        for key in counts.keys():
            buckets[counts[key]].append(key)
        
        print(buckets)
        for i in range(len(nums), -1, -1):
            numbers = buckets[i]
            print(numbers)
            for number in numbers:
                if len(response) < k:
                    response.append(number)
                # else:
                #     return response
        return response
