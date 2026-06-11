class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            total = [0]*26
            for letter in word:
                total[ord(letter)-ord('a')] += 1
            groups[tuple(total)].append(word)
        return list(groups.values())