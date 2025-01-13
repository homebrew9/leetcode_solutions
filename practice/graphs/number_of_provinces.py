# =================================================================
# DFS traversal
# =================================================================

from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            if node not in visited:
                return
            for x in hsh[node]:
                if x not in visited:
                    visited.add(x)
                    dfs(x)
        N = len(isConnected)
        hsh = defaultdict(list)
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    hsh[i] += [j]
        res = 0
        visited = set()
        for i in range(N):
            if i not in visited:
                visited.add(i)
                res += 1
                dfs(i)
        return res

# Main section
for isConnected in [
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,1]],
                   ]:
    print(f'isConnected = {isConnected}')
    sol = Solution()
    r = sol.findCircleNum(isConnected)
    print(f'r = {r}')
    print('==================')


# =================================================================
# BFS traversal
# =================================================================

from collections import defaultdict, deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(node):
            dq = deque()
            dq.append(node)
            while dq:
                size = len(dq)
                for _ in range(size):
                    cur = dq[0]
                    for x in hsh[cur]:
                        if x not in visited:
                            visited.add(x)
                            dq.append(x)
                    dq.popleft()
        N = len(isConnected)
        hsh = defaultdict(list)
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    hsh[i] += [j]
        visited = set()
        res = 0
        for i in range(N):
            if i not in visited:
                res += 1
                visited.add(i)
                bfs(i)
        return res

# Main section
for isConnected in [
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,1]],
                   ]:
    print(f'isConnected = {isConnected}')
    sol = Solution()
    r = sol.findCircleNum(isConnected)
    print(f'r = {r}')
    print('==================')


# =================================================================
# Union-Find or Disjoint Set Union
# =================================================================


