class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) < len(nums2):
            li1 = nums1
            li2 = nums2
        else:
            li1 = nums2
            li2 = nums1

        l = 0
        r = len(li1)-1
        while True:
            mid = (l+r) // 2
            li1l = li1[mid] if mid >= 0 else float('-inf')
            li1r = li1[mid+1] if mid+1 < len(li1) else float('inf')
            li2l = li2[half-mid-2] if half-mid-2 >= 0 else float('-inf')
            li2r = li2[half-mid-1] if half-mid-1 < len(li2) else float('inf')

            if li1l <= li2r and li2l <= li1r:
                if total % 2:
                    return min(li1r, li2r)
                else:
                    return (max(li1l, li2l) + min(li1r, li2r)) / 2
            elif li1l > li2r:
                r = mid - 1
            else:
                l = mid + 1
        
