class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <=1:
                return nums

            mid = len(nums) // 2

            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)
        
        def merge(left, right):
            response = []
            left_count, right_count = 0, 0

            while left_count <len(left) and right_count < len(right):
                if left[left_count] <= right[right_count]:
                    response.append(left[left_count])
                    left_count +=1
                else:
                    response.append(right[right_count])
                    right_count += 1
            response.extend(left[left_count:])
            response.extend(right[right_count:])

            return response

        return merge_sort(nums)