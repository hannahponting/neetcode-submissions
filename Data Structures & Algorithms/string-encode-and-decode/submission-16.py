class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(f"{len(word)}#{word}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        '3#THE4#BEAD'
        result = []
        while s:
            i = 0
            while s[i] != '#':
                i += 1
            count = int(s[:i])
            result.append(s[i+1:count+i+1])
            s = s[count+i+1:]
        return result
