from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find with path compression algorithm
        def find(x):
            if nodes[x] == x:
                return x
            val = find(nodes[x])
            nodes[x] = val
            return val
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return 0
            if rank[root_x] > rank[root_y]:
                rank[root_x] += rank[root_y]
                nodes[root_x] = root_y
            else:
                rank[root_y] += rank[root_x]
                nodes[root_y] = root_x
            return 1
        nodes = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        res = n
        for u, v in edges:
            res -= union(u, v)
        return res

# Main section
for n, edges in [
                   (5, [[0,1],[1,2],[3,4]]),
                   (5, [[0,1],[1,2],[2,3],[3,4]]),
                   (3, [[2,1],[1,0]]),
                   (4, [[2,3],[1,2],[1,3]]),
                   (3, [[2,1],[1,0],[0,2]]),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.countComponents(n, edges)
    print(f'r = {r}')
    print('========================')

