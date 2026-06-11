class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for word in strs:
            response = response + str(len(word)) + '#' + word
        return response

    def decode(self, s: str) -> List[str]:
        i = 0
        length = ''
        result = []
        while i < len(s):
            if s[i] != '#':
                length = length + s[i]
                i = i + 1
            else:
                length = int(length)
                word = s[i+1:i+1+length]
                result.append(word)
                i = i+1+length
                length = ''
        return result
