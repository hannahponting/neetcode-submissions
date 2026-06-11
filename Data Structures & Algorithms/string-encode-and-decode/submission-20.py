class Solution:

    def encode(self, strs: List[str]) -> str:
        response = []
        for s in strs:
            response.append(f"{len(s)}#{s}")
        return "".join(response)

    def decode(self, s: str) -> List[str]:
        response = []
        pointer = 0
        while s:
            while s[pointer] != '#':
                pointer += 1
            count = int(s[:pointer])
            word = s[pointer+1:pointer+1+count]
            s = s[pointer+1+count:]
            response.append(word)
            pointer = 0
        return response