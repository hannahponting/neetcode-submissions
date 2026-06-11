class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A = nums1 if len(nums1) < len(nums2) else nums2
        B = nums2 if len(nums1) < len(nums2) else nums1

        l = 0
        r = len(A)

        while True:
            mid = (l+r) // 2
            leftA = A[mid-1] if mid-1 >= 0 else float('-inf')
            rightA = A[mid] if mid < len(A) else float('inf')
            leftB = B[half-mid-1] if half-mid >= 0 else float('-inf')
            rightB = B[half-mid] if half-mid < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    print("even")
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    print("odd")
                    return min(rightA, rightB)
            elif leftA > rightB:
                r = mid -1
            else:
                l = mid + 1
