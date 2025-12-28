from typing import List, Optional

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
            [  4 ,  3 ,  2 ,| -1 ]
            [  3 ,  2 ,  1 ,| -1 ]
                       +----+
            [  1 ,  1 ,| -1 , -2 ]
            -----------+
            [ -1 , -1 ,  -2 , -3 ]
            Brute force and Binary Search are easy solutions. The trick to
            solving the problem in O(m+n) is to understand the following:
            "If at row r, the first negative element is at column c, then in
            row (r + 1), the first negative element must be at column c or earlier."
            That's because the integers are reverse sorted row-wise as well as column-wise.
            So now we can traverse the grid from top-right to left-bottom, in a step-like
            fashion - going left and down - looking for first negative elements per row.
            The total steps cannot be more than (m + n) in that case.
        '''
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        # We start with the assumption that the first negative element is at last column index.
        neg_index = cols - 1
        for row in grid:
            while neg_index >= 0 and row[neg_index] < 0:
                neg_index -= 1
            # So now for the current row, everything from columns neg_index+1 onwards is negative.
            res += cols - 1 - neg_index
        return res

# Main section
for grid in [
               [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
               [[3,2],[1,0]],
               [[17,15,15,11,8,3,2],[14,13,9,9,7,1,-1],[12,11,8,5,1,0,-3],[8,7,7,3,0,-2,-5],[5,5,3,1,-1,-3,-9]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.countNegatives(grid)
    print(f'r = {r}')
    print('====================')



