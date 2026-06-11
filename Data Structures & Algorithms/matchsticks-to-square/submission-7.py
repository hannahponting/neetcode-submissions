class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        sides = [0] * 4
        sideL = total // 4

        matchsticks = sorted(matchsticks, reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= sideL:
                    sides[j] = sides[j] + matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]= sides[j] - matchsticks[i]     
            return False
        return backtrack(0)

