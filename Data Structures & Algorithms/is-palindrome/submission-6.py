class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", '').replace("!", '').replace("?", '').replace(",", '').replace(".", '').replace("'", '').replace('"', '').replace(":", '')
        p1 = 0 
        p2 = len(s)-1
        while p1 < p2:
            print(p1, p2, s[p1], s[p2])
            if s[p1] in "!?,.'":
                p1 = p1+1
            if s[p2] in "!?,.'":
                p2 = p2-1
            if s[p1] != s[p2]:
                return False
            p1 = p1 + 1
            p2 = p2 - 1
        return True

    def letter(a):
        a 