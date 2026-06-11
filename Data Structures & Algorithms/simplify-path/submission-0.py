class Solution:
    def simplifyPath(self, path: str) -> str:
        l = 0
        result = []
        while l < len(path)-1 and path:
            while l < len(path)-1 and path[l] == '/':
                l += 1
            r = l
            while r < len(path) and path[r] != '/':
                r += 1
            word = path[l:r]
            if word == '..':
                if result:
                    result.pop()
            elif word != '.' and word != '':
                result.append(word)
            path = path[r:]
            l = 0
            print(result)
        return '/'+'/'.join(result)


