from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if x == nodes[x]:
                return x
            return find(nodes[x])
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX < rootY:
                for i, v in enumerate(nodes):
                    if v == rootY:
                        nodes[i] = rootX
            elif rootY < rootX:
                for i, v in enumerate(nodes):
                    if v == rootX:
                        nodes[i] = rootY
        nodes = [i for i in range(n)]
        for x, y in edges:
            if nodes[x] == nodes[y]:
                return False
            union(x, y)
        return len(set(nodes)) == 1

# Main section
for n, edges in [
                   (5, [[0,1],[0,2],[0,3],[1,4]]),
                   (5, [[0,1],[1,2],[2,3],[1,3],[1,4]]),
                   (3, [[0,2],[2,1],[1,0]]),
                   (4, [[0,1],[2,3]]),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.validTree(n, edges)
    print(f'r = {r}')
    print('==============================')


