from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = defaultdict(list)
        for i in range(len(nums)):
            results[str(nums[i])].append(i+1)
        
        result_list = []
        for i in results.keys():
            result_list.append((len(results[i]), i))
        
        results_list = sorted(result_list)
        # print(results_list)
        result_list_final =[]
        while len(result_list_final) < k:
            print(results_list)
            print(results_list[-1][1])
            result_list_final.append(int(results_list[-1][1]))
            results_list.pop(-1)
        return result_list_final



        