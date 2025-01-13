from typing import List
from collections import defaultdict, deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            #print(f'\t\tnode, visited = {node}, {self.visited}')
            if node not in self.visited:
                return
            for x in self.hsh[node]:
                if x not in self.visited:
                    self.visited.add(x)
                    dfs(x)
        self.hsh = defaultdict(list)
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    self.hsh[i] += [j]
        #print(f'\thsh = {self.hsh}')
        self.visited = set()
        N = len(isConnected)
        res = 0
        for i in range(N):
            #print(f'\ti, res, visited = {i}, {res}, {self.visited}')
            if i not in self.visited:
                res += 1
                self.visited.add(i)
                dfs(i)
        return res
    def findCircleNum_1(self, isConnected: List[List[int]]) -> int:
        def bfs(node):
            dq = deque()
            dq.append(node)
            while dq:
                size = len(dq)
                for _ in range(size):
                    cur = dq.popleft()
                    for x in self.hsh[cur]:
                        if x not in self.visited:
                            self.visited.add(x)
                            dq.append(x)
        self.hsh = defaultdict(list)
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    self.hsh[i] += [j]
        #print(f'\thsh = {self.hsh}')
        N = len(isConnected)
        self.visited = set()
        res = 0
        for i in range(N):
            #print(f'\ti, res, visited = {i}, {res}, {self.visited}')
            if i not in self.visited:
                res += 1
                self.visited.add(i)
                bfs(i)
        return res
    # Incorrect implementation of Union-Find. The code is based on the code in scaler.com; it
    # returns incorrect values as compared to DFS/BFS for the last 3 test cases.
    # 6/23/23 => ok, I found out the reason it was returning incorrect values. The union 
    # function must return a boolean value that helps in calculating how many were union'ed.
    # The final result is then N - cnt.
    def findCircleNum_2(self, isConnected: List[List[int]]) -> int:
        def find(u):
            if parent[u] == u:
                return u
            return find(parent[u])
        def union(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
                return True
            return False
        N = len(isConnected)
        parent = [i for i in range(N)]
        cnt = 0
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    cnt += union(i, j)
        return N - cnt
    def findCircleNum_3(self, isConnected: List[List[int]]) -> int:
        # Using Union-Find algorithm with a list (less efficient than a tree)
        # This algorithm works.
        def find(u):
            while parent[u] != u:
                u = parent[u]
            return u
        def union(u, v):
            u1 = find(u)
            v1 = find(v)
            if u1 == v1:
                return False
            parent[v1] = u1
            return True
        N = len(isConnected)
        cnt = 0
        parent = [i for i in range(N)]
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    ret = union(i, j)
                    if ret:
                        cnt += 1
        return N - cnt

# Main section
for isConnected in [
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]],
                      [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[1,1,0],[1,1,0],[0,0,1]],
                      [[1,0,0],[0,1,0],[0,0,1]],
                      [[1,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,1]],
                      [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],
                      [[1,1,1,0,1,1,1,0,0,0],[1,1,0,0,0,0,0,1,0,0],[1,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0],[1,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,1,1,1]],
                   ]:
    print(f'isConnected = {isConnected}')
    sol = Solution()
    r = sol.findCircleNum(isConnected)
    r1 = sol.findCircleNum_1(isConnected)
    r2 = sol.findCircleNum_2(isConnected)
    r3 = sol.findCircleNum_3(isConnected)
    print(f'r  (DFS)    = {r}')
    print(f'r1 (BFS)    = {r1}')
    print(f'r2 (UF/QU1) = {r2}')
    print(f'r3 (UF/QU2) = {r3}')
    print('=======================')


