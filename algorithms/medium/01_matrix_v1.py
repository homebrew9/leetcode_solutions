from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            if r < 0 or r > rows - 1:
                return
            if c < 0 or c > cols - 1:
                return
            print(f'\t\tNow at: (r, c) = ({r}, {c})')
            visited[r][c] = True
            print(f'\t\tvisited = {visited}')
            if 0 <= r-1 < rows and not visited[r-1][c]:
                dfs(r-1, c)
            if 0 <= r+1 < rows and not visited[r+1][c]:
                dfs(r+1, c)
            if 0 <= c-1 < cols and not visited[r][c-1]:
                dfs(r, c-1)
            if 0 <= c+1 < cols and not visited[r][c+1]:
                dfs(r, c+1)

        rows = len(mat)
        cols = len(mat[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    print(f'\t(r, c) = ({r}, {c})')
                    dfs(r, c)
        return mat

# Main section
for mat in [
              [[1,1,1],[1,1,1],[1,1,0]],
              #[[0,0,0],[0,1,0],[0,0,0]],
              #[[0,0,0],[0,1,0],[1,1,1]],
              #[[0,0,0,0,1],[0,1,0,1,1],[1,0,1,0,1],[0,0,1,1,0]],
              #[[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]],
           ]:
    print(f'mat = {mat}')
    #for item in mat:
    #    print(item)
    sol = Solution()
    r = sol.updateMatrix(mat)
    print(f'r = {r}')
    #for item in r:
    #    print(item)
    print('================')
    #exp = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    #for item in exp:
    #    print(item)


