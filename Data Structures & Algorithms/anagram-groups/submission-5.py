class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_so_far = defaultdict(list)

        for word in strs:
            letters = [0]*26
            for letter in word:
                letters[ord(letter)-ord('a')] = letters[ord(letter)-ord('a')] + 1
            seen_so_far[str(letters)].append(word)
        return list(seen_so_far.values())