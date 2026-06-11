class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count = defaultdict(int)
        for value in nums:
            seen_count[value] += 1

        count_as_key = defaultdict(list)
        for key, number in seen_count.items():
            count_as_key[number].append(key)
        counts = sorted(count_as_key, reverse=True)
        response =[]
        for count in counts:
            for value in count_as_key[count]:
                response.append(value)
                if len(response) == k:
                    return response
        

