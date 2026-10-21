class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        min_dist = [float("inf")]*n
        visited = set()

        min_dist[0]=0
        total = 0
        for _ in range(n):
            cur = -1
            for i in range(n):
                if i not in visited:
                    if cur == -1 or min_dist[i]<min_dist[cur]:
                        cur=i
            visited.add(cur)
            total+=min_dist[cur]
            x1,y1=points[cur]

            for i in range(n):
                if  i not in visited:
                    x2,y2 =points[i]
                    distance =abs(x1-x2)+abs(y1-y2)
                    min_dist[i] = min(min_dist[i],distance)
        return total