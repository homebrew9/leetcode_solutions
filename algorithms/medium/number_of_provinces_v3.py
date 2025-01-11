from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            xset = find(x)
            yset = find(y)
            if xset == yset:
                return
            if rank[xset] < rank[yset]:
                parent[xset] = yset
            elif rank[yset] < rank[xset]:
                parent[yset] = xset
            else:
                parent[yset] = xset
                rank[xset] += 1

        N = len(isConnected)
        parent = [i for i in range(N)]
        rank = [0 for _ in range(N)]
        numberOfComponents = N
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    numberOfComponents -= 1
                    union(i, j)
        return numberOfComponents

# Main section
for isConnected in [
                      [[1,1,0],[1,1,0],[0,0,1]],
                      [[1,0,0],[0,1,0],[0,0,1]],
                      [[1,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,1]],
                      [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],
                   ]:
    print(f'isConnected = {isConnected}')
    sol = Solution()
    r = sol.findCircleNum(isConnected)
    print(f'r = {r}')
    print('==================')


