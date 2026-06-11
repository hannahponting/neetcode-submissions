class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        result = ''.join(res)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s)-1:
            start = i
            while s[i] != '#':
                i += 1
            length = int(s[start:i])
            words.append(s[i+1:i+1+length])
            i = i+1+length
        return words
            