class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs = sorted(strs) 
        prefix = strs[0]
        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
        return prefix
            