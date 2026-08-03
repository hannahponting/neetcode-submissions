class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        seen = set()
        res = defaultdict(list)
        route = []

        for src, dst in tickets:
            heapq.heappush(res[src], dst)
        
        def dfs(src):
            while res[src]:
                dfs(heapq.heappop(res[src]))
            route.append(src)

        dfs("JFK")
        return route[::-1]
