class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters_s = {}
        for i in s:
            if characters_s.get(i):
                characters_s[i] = characters_s[i] + 1
            else:
                characters_s[i] = 1
        characters_t = {}
        for i in t:
            if characters_t.get(i):
                characters_t[i] = characters_t[i] + 1
            else:
                characters_t[i] = 1
        return characters_s == characters_t
        