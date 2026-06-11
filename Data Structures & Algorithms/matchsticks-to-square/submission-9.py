class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks = sorted(matchsticks, reverse=True)
        total = sum(matchsticks)
        side = total / 4

        if total % 4 != 0:
            return False
        if matchsticks[0] > side:
            return False
        
        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return dfs(0)