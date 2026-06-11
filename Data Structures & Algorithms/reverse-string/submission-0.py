class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        while l < len(s)//2:
            left = s[l]
            right = s[-(l+1)]
            s[l] = right
            s[-(l+1)] = left
            l += 1