from typing import List
from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # BFS solution
        hsh = defaultdict(list)
        for u, v in edges:
            hsh[u] += [v]
            hsh[v] += [u]
        if len(hsh) == 0:
            return n
        # Append the leaf nodes to dq
        dq = deque()
        for key, val in hsh.items():
            if len(val) == 1:
                dq.append(key)
        component_count = 0
        while dq:
            curr = dq.popleft()
            neighbor = -1
            if len(hsh[curr]) > 0:
                neighbor = hsh[curr][0]
                hsh[curr].remove(neighbor)
                hsh[neighbor].remove(curr)
            rem = values[curr] % k
            if rem == 0:
                component_count += 1
            elif neighbor in hsh:
                values[neighbor] += rem
            # Append neighbor to dq if it has become a leaf now.
            if neighbor in hsh and len(hsh[neighbor]) == 1:
                dq.append(neighbor)
        return component_count

# Main section
for n, edges, values, k in [
                              (5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6),
                              (7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3),
                              (1, [], [0], 1),
                           ]:
    print(f'n, edges, values, k = {n}, {edges}, {values}, {k}')
    sol = Solution()
    r = sol.maxKDivisibleComponents(n, edges, values, k)
    print(f'r = {r}')
    print('===================')


