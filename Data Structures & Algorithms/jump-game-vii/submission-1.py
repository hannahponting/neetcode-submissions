class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        seen = set()

        while q:
            i = q.popleft()
            for j in range(i + minJump, min(i + maxJump + 1, len(s))):
                if s[j] == "0" and j not in seen:
                    q.append(j)
                    seen.add(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        return False