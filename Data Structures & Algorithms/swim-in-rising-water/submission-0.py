class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        heap=[(grid[0][0], 0, 0)]
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r,c))

            if r==n-1 and c==n-1:
                return time
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=n or nc<0 or nc>=n:
                    continue
                if  (nr,nc) in visited:
                    continue
                new_time = max(time, grid[nr][nc])
                heapq.heappush(heap, (new_time, nr, nc))
        return -1