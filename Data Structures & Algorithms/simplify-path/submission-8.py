class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        result = []
        print(path)

        for i in range(len(path)):
            if path[i] == '..':
                if result:
                    result.pop()
            elif path[i] == '.' or path[i] == '':
                continue
            else:
                result.append(path[i])
        print(result)
        return '/'+'/'.join(result)
