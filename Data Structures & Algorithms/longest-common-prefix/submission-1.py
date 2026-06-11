class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        response = ""
        for i in range(1, len(strs[0])+1):
            prefixes = set([word[:i] for word in strs])
            if len(prefixes) == 1:
                response = strs[0][:i]
            else:
                break
        return response
