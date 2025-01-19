#
# Naive iteration, not too fancy!
#
from typing import List
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rows1, cols1 = len(mat1), len(mat1[0])
        rows2, cols2 = len(mat2), len(mat2[0])
        # It is guaranteed that cols1 = rows2
        mat = [[0 for _ in range(cols2)] for _ in range(rows1)]
        for r in range(rows1):
            arr1 = mat1[r]
            for c in range(cols2):
                arr2 = list()
                for x in range(rows2):
                    arr2.append(mat2[x][c])
                mat[r][c] = sum([p * q for p, q in zip(arr1, arr2)])
        return mat

# Main section
for mat1, mat2 in [
                     ([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]),
                     ([[0]], [[0]]),
                     ([[1,0,0],[-1,0,3]], [[7,0,0,0,1],[0,0,0,1,0],[0,2,0,0,0]]),
                  ]:
    print(f'mat1, mat2 = {mat1}, {mat2}')
    sol = Solution()
    r = sol.multiply(mat1, mat2)
    print(f'r = {r}')
    print('==================')


