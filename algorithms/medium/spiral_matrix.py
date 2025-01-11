from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def fetchSpiralNumbers(matrix, rows, cols, r, c):
            arr = list()
            # right  = (r, cols - c - 1)
            # bottom = (rows - r - 1, cols - c - 1)
            # left   = (rows - r - 1, c)
            # top    = (r + 1, c)
            i, j = r, c
            while j <= cols - c - 1:
                print(f'\tInside 1st while...')
                #print(f'\ti, j, cols-r-1 = {i}, {j}, {cols-i-1}')
                arr.append(matrix[i][j])
                matrix[i][j] = -999
                j += 1
                #print(f'\tarr = {arr}')
            print(f'\ti, j, arr = {i}, {j}, {arr}')
            j -= 1
            i += 1
            print(f'\tAfter adj; i, j, rows-r-1 = {i}, {j}, {rows-r-1}')
            if i > rows - r - 1:
                return arr
            while i <= rows - r - 1:
                print(f'\tInside 2nd while...')
                #print(f'\ti, j, rows-r-1 = {i}, {j}, {rows-i-1}')
                arr.append(matrix[i][j])
                matrix[i][j] = -999
                i += 1
                #print(f'\tarr = {arr}')
            print(f'\ti, j, arr = {i}, {j}, {arr}')
            i -= 1
            j -= 1
            while j >= c:
                print(f'\tInside 3rd while...')
                arr.append(matrix[i][j])
                matrix[i][j] = -999
                j -= 1
            print(f'\ti, j, arr = {i}, {j}, {arr}')
            j += 1
            i -= 1
            #print(f'\ti, j, arr = {i}, {j}, {arr}')
            while i >= r + 1:
                print(f'\tInside 4th while...')
                arr.append(matrix[i][j])
                matrix[i][j] = -999
                i -= 1
            print(f'\tReturning arr = {arr}')
            print(f'\t=====')
            return arr

        rows = len(matrix)
        cols = len(matrix[0])
        res = list()

        if cols == 1:
            for r in range(rows):
                res += [matrix[r][0]]
            return res

        for r in range(rows):
            for c in range(cols):
                if r == c:
                    #print(f'r, c, matrix = {r}, {c}, {matrix}')
                    if matrix[r][c] == -999:
                        break
                    if cols - c - 1 < c:
                        break
                    elif cols - c - 1 == c:
                        i = r
                        while i <= rows - r - 1:
                            res += [matrix[i][c]]
                            i += 1
                        break
                    else:
                        res += fetchSpiralNumbers(matrix, rows, cols, r, c)
        return res

# Main section
for matrix in [
                 #[[1,2,3],[4,5,6],[7,8,9]],
                 #[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
                 #[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
                 #[[1,2],[3,4]],
                 #[[1]],
                 #[[1,2]],
                 #[[1],[2]],
                 #[[1],[2],[3],[4],[5]],
                 #[[2,5,8],[4,0,-1]],
                 [[2,3,4],[5,6,7],[8,9,10],[11,12,13]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.spiralOrder(matrix)
    print(f'r = {r}')
    print('================')

