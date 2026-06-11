class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1] # which wins
                if diff < 0: # if incoming one wins remove last
                    stack.pop()
                elif diff > 0:
                    a = 0  # if incoming current one wins zero incoming
                else:
                    a = 0
                    stack.pop() # do both as equal
            if a != 0:
                stack.append(a)
        return stack


