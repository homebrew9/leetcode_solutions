from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def get_numbers(r, c):
            arr = list()
            while r >= 0 and c < cols:
                arr.append(mat[r][c])
                r -= 1
                c += 1
            return arr
        rows = len(mat)
        cols = len(mat[0])
        res = list()
        for r in range(rows):
            tmp = get_numbers(r, 0)
            if r % 2 == 0:
                res.extend(tmp)
            else:
                res.extend(tmp[::-1])
        for c in range(1, cols):
            tmp = get_numbers(rows - 1, c)
            if (rows - 1 + c) % 2 == 0:
                res.extend(tmp)
            else:
                res.extend(tmp[::-1])
        return res

# Main section
for mat in [
              [[1,2,3],[4,5,6],[7,8,9]],
              [[1,2],[3,4]],
           ]:
    print(f'mat = {mat}')
    sol = Solution()
    r = sol.findDiagonalOrder(mat)
    print(f'r   = {r}')
    print('==================')








