from typing import List

class Solution:
    # Both functions work correctly
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        cols = len(colsum)
        grid = [[0 for _ in range(cols)] for _ in range(2)]
        for i, v in enumerate(colsum):
            if v == 2:
                if upper == 0 or lower == 0:
                    return []
                grid[0][i] = 1
                grid[1][i] = 1
                upper -= 1
                lower -= 1
        for i, v in enumerate(colsum):
            if v == 1:
                if upper == 0 and lower == 0:
                    return []
                if upper > 0:
                    grid[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    grid[1][i] = 1
                    lower -= 1
        return grid
    def reconstructMatrix_1(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        cols = len(colsum)
        grid = [[0 for _ in range(cols)] for _ in range(2)]
        for i, v in enumerate(colsum):
            if v == 2:
                grid[0][i] = 1
                grid[1][i] = 1
                upper -= 1
                lower -= 1
            elif v == 1:
                if upper > lower:
                    grid[0][i] = 1
                    upper -= 1
                else:
                    grid[1][i] = 1
                    lower -= 1
        if upper == 0 and lower == 0:
            return grid
        else:
            return []

# Main section
for upper, lower, colSum in [
                               (2, 1, [1,1,1]),
                               (2, 3, [2,2,1,1]),
                               (5, 5, [2,1,2,0,1,0,1,2,0,1]),
                               (4, 2, [1,2,1,2,0]),
                               (9, 2, [0,1,2,0,0,0,0,0,2,1,2,1,2]),
                            ]:
    print(f'upper, lower, colSum = {upper}, {lower}, {colSum}')
    sol = Solution()
    r = sol.reconstructMatrix(upper, lower, colSum)
    print(f'r  = {r}')
    r1 = sol.reconstructMatrix_1(upper, lower, colSum)
    print(f'r1 = {r1}')
    print('=================')


