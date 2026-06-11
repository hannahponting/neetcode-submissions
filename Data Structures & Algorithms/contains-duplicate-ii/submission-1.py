class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list)

        for index, num in enumerate(nums):
            if len(seen[num]) > 0:
                for second_index in seen[num]:
                    if index - second_index <= k or index - second_index <= - k:
                        return True
            seen[num].append(index)
        return False
            



    
