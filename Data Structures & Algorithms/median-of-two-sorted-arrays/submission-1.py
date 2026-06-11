class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total // 2
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            B = nums1
            A = nums2

        l = 0
        r = len(A) - 1
        while True:
            i = (l + r)// 2
            LeftA = A[i] if i >= 0 else float('-inf')
            LeftB = B[half-i-2] if half-i-2 >= 0 else float('-inf')
            RightA = A[i+1] if i+1 < len(A) else float('inf')
            RightB = B[half-i-1] if half-i-1 < len(B) else float('inf')

            if LeftA <= RightB and LeftB <= RightA:
                if total % 2: 
                    return min(RightA, RightB)
                else:
                    return (max(LeftA, LeftB) + min(RightA, RightB)) / 2
            elif LeftA > RightB:
                r = i - 1
            else:
                l = i + 1