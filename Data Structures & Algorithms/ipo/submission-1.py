class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: List[int],
        capital: List[int]
    ) -> int:

        projects = []
        for c, p in zip(capital, profits):
            heapq.heappush(projects, (c, p))

        available = []
        current_capital = w

        for _ in range(k):
            while projects and projects[0][0] <= current_capital:
                c, p = heapq.heappop(projects)
                heapq.heappush(available, -p)
            if not available:
                break
            current_capital += -heapq.heappop(available)

        return current_capital