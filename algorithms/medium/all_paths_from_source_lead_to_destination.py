from typing import List

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            if state[node] is not None:
                return state[node]
            if len(adj[node]) == 0:
                return node == destination
            state[node] = False # type: ignore
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            state[node] = True # type: ignore
            return True
        adj = [list() for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        state = [None] * n
        return dfs(source) # type: ignore

# Main section
for n, edges, source, destination in [
                                        (3, [[0,1],[0,2]], 0, 2),
                                        (4, [[0,1],[0,3],[1,2],[2,1]], 0, 3),
                                        (4, [[0,1],[0,2],[1,3],[2,3]], 0, 3),
                                     ]:
    print(f'n, edges, source, destination = {n}, {edges}, {source}, {destination}')
    sol = Solution()
    r = sol.leadsToDestination(n, edges, source, destination)
    print(f'r = {r}')
    print('=====================')






