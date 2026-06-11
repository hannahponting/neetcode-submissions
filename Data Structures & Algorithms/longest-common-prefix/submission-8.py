class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(1, len(sorted(strs)[0])+1):
            seen = set()
            for word in strs:
                seen.add(word[:i])
            print(seen)
            if len(seen) != 1:
                return strs[0][:i-1]
            if i == len(sorted(strs)[0]):
                return strs[0][:i]
        return ""
            