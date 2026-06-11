class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string + str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        response = []
        while s:
            length = ''
            while True:
                if s[0] != '#':
                    length = length + s[0]
                    s = s[1:]
                else:
                    s = s[1:]
                    break
            length = int(length)
            response.append(s[:length])
            s = s[length:]
        return response

