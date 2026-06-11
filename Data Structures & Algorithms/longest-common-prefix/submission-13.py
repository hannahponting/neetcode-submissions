class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs)
        prefix = strs[0]
        print(prefix)

        while prefix and not strs[-1].startswith(prefix):
            prefix = prefix[:-1]
            print(prefix)
        return prefix