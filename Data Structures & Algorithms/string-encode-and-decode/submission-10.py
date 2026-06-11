class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if strs == [""]:
            return ".../..."
        encoded_string = '.../...'.join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == ".../...":
            return [""]
        return s.split(".../...")

        
