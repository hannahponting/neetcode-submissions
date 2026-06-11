class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        results = []

        for i in asteroids:
            while results and i < 0 < results[-1]:
                if -i > results[-1]:
                    results.pop() 
                    continue
                elif results[-1] == -i:
                    results.pop()
                break
            else:
                results.append(i)
        return results