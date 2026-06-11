class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        max_sequence = 0
        for num in nums:
            numbers.add(num)
        
        for num in numbers:
            if num-1 not in numbers:
                sequence = 1
                i = 1
                while num+i in numbers:
                    sequence +=1 
                    i += 1
                max_sequence = max(max_sequence, sequence)
        return max_sequence
