class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(f'{len(word)}#{word}')
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while s:
            if s[i] != '#':
                i += 1
            else:
                length = int(s[:i])
                word = s[i+1: i+1+length]
                result.append(word)
                s = s[i+1+length:]
                i = 0
        return result

