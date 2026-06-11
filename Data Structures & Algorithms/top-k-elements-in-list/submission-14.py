class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count = defaultdict(int)

        for index, value in enumerate(nums):
            seen_count[value] += 1

        count_as_key = defaultdict(list)
        for key in seen_count:
            count_as_key[seen_count[key]].append(key)
        counts = sorted(count_as_key.keys(), reverse=True)
        response =[]
        for i in counts:
            print(count_as_key[i])
            for value in count_as_key[i]:
                print(value)
                if len(response) < k:
                    response.append(value)
                else:
                    return response
        return response
        

