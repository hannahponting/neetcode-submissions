class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            print("i:", i)
            for j in range(i+1, len(numbers)):
                print("j:", j)
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
