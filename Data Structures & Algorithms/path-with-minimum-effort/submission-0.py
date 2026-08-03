class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        
        minHeap = [[0, 0, 0]] # [diff, r, c]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            
            visit.add((r,c))
            if r == ROWS - 1 and c == COLS - 1:
                return diff
            
            for dr, dc in directions:
                if dr + r < 0 or dc + c < 0 or dr + r == ROWS  or dc + c == COLS or (dr+r, dc + c) in visit:
                    continue
                heapq.heappush(minHeap, (max(diff, abs(heights[r][c]- heights[r+dr][c+dc])), dr+r, dc+c))



