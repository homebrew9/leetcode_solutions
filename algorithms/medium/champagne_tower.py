#
# Incorrect algorithm. Use simulation to arrive at the solution.
#
import math
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        if poured == 1:
            if query_row == 0:
                return 1
            else:
                return 0
        # Rows up to filled_rows (0-indexed) are filled
        filled_rows = int((math.sqrt(1 + 4*2*poured) - 1)/2) - 1
        if query_row <= filled_rows:
            return 1
        if query_row > filled_rows + 1:
            return 0
        if query_row == 0:
            return poured
        if query_row == 1:
            return 1/2
        denom = 2*query_row
        left_over = poured - (filled_rows+1)*(filled_rows+2)/2
        if query_glass == 0 or query_glass == query_row:
            return 1*left_over/denom
        else:
            return 2*left_over/denom

# Main section
for poured, query_row, query_glass in [
                                         (1, 1, 1),
                                         (2, 1, 1),
                                         (100000009, 33, 17),
                                         (13, 5, 0),
                                         (13, 5, 1),
                                         (13, 5, 2),
                                         (13, 5, 3),
                                         (13, 5, 4),
                                         (13, 5, 5),
                                      ]:
    print(f'poured, query_row, query_glass = {poured}, {query_row}, {query_glass}')
    sol = Solution()
    r = sol.champagneTower(poured, query_row, query_glass)
    print(f'r = {r}')
    print('=================')

