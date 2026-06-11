class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen_nums = {}
        result = []
        for i in range(len(nums)):
            seen_nums[nums[i]] = i

        print(seen_nums)
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            else:
                for j in range(i+1, len(nums)):
                    needed = (- nums[i] - nums[j])
                    print(needed)
                    if needed in seen_nums and seen_nums[needed] not in [i,j]:
                        to_add = sorted([nums[i], nums[j], needed])
                        if to_add not in result:
                            result.append(to_add)
        return result
                
                        

