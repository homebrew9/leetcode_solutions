#
# Simulation approach.
#
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        N = len(queens)
        row, col = king
        seen = set()
        for elem in queens:
            seen.add(tuple(elem))
        res = list()
        for r, c in queens:
            if r == row:
                # travel along the column
                if col > c:
                    i = c + 1
                    while i < col:
                        if (r, i) in seen:
                            break
                        i += 1
                else:
                    i = c - 1
                    while i > col:
                        if (r, i) in seen:
                            break
                        i -= 1
                if i == col:
                    res.append([r, c])
            elif c == col:
                # travel along the row
                if row > r:
                    i = r + 1
                    while i < row:
                        if (i, c) in seen:
                            break
                        i += 1
                else:
                    i = r - 1
                    while i > row:
                        if (i, c) in seen:
                            break
                        i -= 1
                if i == row:
                    res.append([r, c])
            elif abs(r - row) == abs(c - col):
                # travel along the diagonal
                dr = -1 if row < r else 1
                dc = -1 if col < c else 1
                rnew, cnew = r + dr, c + dc
                while (rnew, cnew) not in seen and (rnew, cnew) != (row, col):
                    rnew += dr
                    cnew += dc
                if (rnew, cnew) == (row, col):
                    res.append([r, c])
        return res

# Main section
for queens, king in [
                       ([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]),
                       ([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3]),
                    ]:
    print(f'queens, king = {queens}, {king}')
    sol = Solution()
    r = sol.queensAttacktheKing(queens, king)
    print(f'r = {r}')
    print('======================')


