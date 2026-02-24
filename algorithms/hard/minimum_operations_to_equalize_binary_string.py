from collections import deque
from sortedcontainers import SortedList
from bisect import bisect_left
import math

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n, m = len(s), s.count("0")
        dist = [math.inf] * (n + 1)
        nodeSets = [
            SortedList(range(0, n + 1, 2)),
            SortedList(range(1, n + 1, 2)),
        ]
        q = deque([m])
        dist[m] = 0
        nodeSets[m % 2].remove(m)
        while q:
            m = q.popleft()
            c1, c2 = max(k - n + m, 0), min(m, k)
            lnode, rnode = m + k - 2 * c2, m + k - 2 * c1
            nodeSet = nodeSets[lnode % 2]
            idx = nodeSet.bisect_left(lnode)
            while idx < len(nodeSet) and nodeSet[idx] <= rnode: # type: ignore
                m2 = nodeSet[idx]
                dist[m2] = dist[m] + 1 # type: ignore
                q.append(m2) # type: ignore
                nodeSet.pop(idx)
        return -1 if dist[0] == math.inf else dist[0] # type: ignore

# Main section
for s, k in [
               ('110', 1),
               ('0101', 3),
               ('101', 2),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.minOperations(s, k)
    print(f'r = {r}')
    print('=================================================')
 

