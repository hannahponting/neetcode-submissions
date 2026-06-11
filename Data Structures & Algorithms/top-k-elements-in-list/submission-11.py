class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times_seen = {}
        for i in nums:
            nums_seen = times_seen.get(str(i), 0)
            times_seen[str(i)] = nums_seen + 1

        res = [0]*(len(nums)+1)
        for key in times_seen:
            old_list = res[times_seen[key]]
            if old_list == 0:
                old_list = [key]
            else:
                old_list.append(key)
            res[times_seen[key]] = old_list
        result = []
        for i in range(len(res)-1, 0, -1):
            if res[i] != 0:
                for j in res[i]:
                    result.append(int(j))
            

                if len(result) == k:
                    return result