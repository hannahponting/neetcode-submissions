class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for letter in range(max(len(word1), len(word2))):
            if letter < len(word1):
                result.append(word1[letter])
            if letter < len(word2):
                result.append(word2[letter])
        return ''.join(result)
