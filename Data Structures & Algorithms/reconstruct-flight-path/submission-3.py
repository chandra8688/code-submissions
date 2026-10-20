import heapq
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src],dst)
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

            itinerary.append(airport)
        dfs("JFK")

        return itinerary[::-1]
