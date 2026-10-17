class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent = list(range(n+1))
        size = [1]*(n+1)

        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False

            if size[root_u] <size[root_v]:
                root_u, root_v = root_v, root_u

            parent[root_v] = root_u
            size[root_u] +=size[root_v]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]