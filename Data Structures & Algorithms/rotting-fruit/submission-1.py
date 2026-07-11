class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        q = deque()
        visit = set()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                if grid[r][c] == 1:
                    count += 1

        time = 0
        while q and count:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and (r+dr, c+dc) not in visit and grid[r+dr][c+dc] == 1:
                        count -= 1
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
            time += 1

        if count == 0:
            return time
        else:
            return -1




        
        