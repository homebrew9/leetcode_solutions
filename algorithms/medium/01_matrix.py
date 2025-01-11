#
# Does not work! This is a DP problem.
#
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    tmp = []
                    if 0 <= r - 1 < rows:
                        tmp.append(1 + mat[r-1][c])
                    if 0 <= r + 1 < rows:
                        tmp.append(1 + mat[r+1][c])
                    if 0 <= c - 1 < cols:
                        tmp.append(1 + mat[r][c-1])
                    if 0 <= c + 1 < cols:
                        tmp.append(1 + mat[r][c+1])
                    mat[r][c] = min(tmp)
        return mat

# Main section
for mat in [
              #[[0,0,0],[0,1,0],[0,0,0]],
              #[[0,0,0],[0,1,0],[1,1,1]],
              #[[0,0,0,0,1],[0,1,0,1,1],[1,0,1,0,1],[0,0,1,1,0]],
              [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]],
           ]:
    print(f'mat = {mat}')
    for item in mat:
        print(item)
    sol = Solution()
    r = sol.updateMatrix(mat)
    print(f'r = {r}')
    for item in r:
        print(item)
    print('================')
    #exp = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    #for item in exp:
    #    print(item)

