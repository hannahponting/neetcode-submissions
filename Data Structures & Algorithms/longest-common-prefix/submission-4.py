class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)== 1:
            return strs[0]
        strs = sorted(strs)

        for i in range(min(len(strs[0]), len(strs[-1]))):
           if strs[0][:i+1] != strs[-1][:i+1]:
                return strs[0][:i]
        return strs[0]
