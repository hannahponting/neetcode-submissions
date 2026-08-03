class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = [(grid[0][0], 0, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while res:
            t, x, y = heapq.heappop(res)
            time = max(time, t)

            if x == ROWS-1 and y == COLS-1:
                return time
            
            for cx, cy in directions:
                newx, newy = x+cx, y+cy
                if newx < 0 or newy < 0. or newx == ROWS or newy==COLS or (newx, newy) in seen:
                    continue
                seen.add((newx, newy))
                heapq.heappush(res, (grid[newx][newy], newx, newy))

                
