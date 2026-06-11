class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        print(path)
        for word in path:
            print(stack)
            if word:
                if word == '..':
                    if stack:
                        stack.pop()
                else:
                    if word != '.':
                        stack.append(word)
        return '/'+'/'.join(stack)
