from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def dfs(r, c, direction, rows, cols):
            # Idea is similar to turtle graphics - the turtle moves on the matrix in a
            # predefined pattern and resets the values of visited cells.
            self.res.append(matrix[r][c])
            matrix[r][c] = -999
            if direction == 'r':
                if c+1 >= cols or matrix[r][c+1] == -999:
                    rnext, cnext, direction = r+1, c, 'd'
                else:
                    rnext, cnext = r, c+1
                if 0 <= rnext < rows and 0 <= cnext < cols and matrix[rnext][cnext] != -999:
                    dfs(rnext, cnext, direction, rows, cols)
            elif direction == 'd':
                if r+1 >= rows or matrix[r+1][c] == -999:
                    rnext, cnext, direction = r, c-1, 'l'
                else:
                    rnext, cnext = r+1, c
                if 0 <= rnext < rows and 0 <= cnext < cols and matrix[rnext][cnext] != -999:
                    dfs(rnext, cnext, direction, rows, cols)
            elif direction == 'l':
                if c-1 < 0 or matrix[r][c-1] == -999:
                    rnext, cnext, direction = r-1, c, 'u'
                else:
                    rnext, cnext = r, c-1
                if 0 <= rnext < rows and 0 <= cnext < cols and matrix[rnext][cnext] != -999:
                    dfs(rnext, cnext, direction, rows, cols)
            elif direction == 'u':
                if r-1 < 0 or matrix[r-1][c] == -999:
                    rnext, cnext, direction = r, c+1, 'r'
                else:
                    rnext, cnext = r-1, c
                if 0 <= rnext < rows and 0 <= cnext < cols and matrix[rnext][cnext] != -999:
                    dfs(rnext, cnext, direction, rows, cols)

        rows = len(matrix)
        cols = len(matrix[0])
        self.res = list()
        dfs(0, 0, 'r', rows, cols)
        return self.res

# Main section
for matrix in [
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
                 [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
                 [[1,2],[3,4]],
                 [[1]],
                 [[1,2]],
                 [[1],[2]],
                 [[1],[2],[3],[4],[5]],
                 [[2,5,8],[4,0,-1]],
                 [[2,3,4],[5,6,7],[8,9,10],[11,12,13]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.spiralOrder(matrix)
    print(f'r = {r}')
    print('================')


