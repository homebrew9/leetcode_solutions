from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # A node that receives an edge of the DAG cannot be the champion.
        # We simply need an array of booleans. No hashes, no sets!
        # There are other ways of solving it too e.g. BFS, indegree count etc.
        arr = [True for _ in range(n)]
        for u, v in edges:
            arr[v] = False
        if arr.count(True) != 1:
            return -1
        return arr.index(True)

# Main section
for n, edges in [
                   (3, [[0,1],[1,2]]),
                   (4, [[0,2],[1,3],[1,2]]),
                   (3, [[0,1]]),
                   (1, []),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.findChampion(n, edges)
    print(f'r = {r}')
    print('==================')


