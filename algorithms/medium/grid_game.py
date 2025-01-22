from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Create prefix sum arrays - R-to-L for Row 0 and L-to-R for Row 1.
        # At each index, the robot 1 has to make a decision to go from Row 0 to Row 1. If it
        # does, then robot 2 will collect the max(upper_pfx_row, lower_pfx_row). So find out
        # this value i.e. max(upper_pfx_row, lower_pfx_row) for each index and compare it with a global
        # minimum. The global min is the answer; it is the min of all the individual max per index.
        N = len(grid[0])
        pfx_right = [0 for _ in range(N)]
        for i in range(N-1, -1, -1):
            pfx_right[i] = grid[0][i] if i == N - 1 else pfx_right[i+1] + grid[0][i]
        pfx_left = [0 for _ in range(N)]
        for i in range(N):
            pfx_left[i] = grid[1][i] if i == 0 else pfx_left[i-1] + grid[1][i]

        # Note that a corner case is when there is only 1 column. Robot 1 will collect all points in
        # that case and robot 2 will collect 0. We can handle this case at the top or add the if
        # condition while setting val for the case i == 0, as done below.
        res = float('inf')
        for i in range(N):
            if i == 0:
                val = 0 if i + 1 >= N else pfx_right[i+1]
            elif i == N - 1:
                val = pfx_left[i-1]
            else:
                val = max(pfx_right[i+1], pfx_left[i-1])
            res = min(res, val)
        return res

# Main section
for grid in [
               [[2,5,4],[1,5,1]],
               [[3,3,1],[8,5,2]],
               [[1,3,1,15],[1,3,3,1]],
               [[2,1,4,5], [6,8,10,5]],
               [[9,3,6,1,7,9,10], [10,9,5,3,9,3,8]],
               [[1,96,75,36,31,78,97,50,10,15,81,74,68,25,81,12,10,19,32,65,12,59,43,29,8,81,16,34,5,75,34,23,83,86,35,55,84,22,79,98,23,47,53,90,10,14,12,66,90,80], [11,13,92,2,7,71,43,60,48,20,39,82,59,58,72,87,83,98,62,67,52,18,76,14,84,24,23,41,41,19,50,87,43,48,34,29,10,10,75,3,80,30,8,14,3,97,28,51,87,78]],
               [[73,55,49,1,15,39,65,87,4,46,2,31,66,58,77,75,6,96,10,49], [87,76,82,46,86,26,50,62,33,32,22,30,53,2,35,3,48,41,99,25]],
               [[6,9,5,4,8,10,6,2,6,9,4,7,9,9,4,3,4,5,3,10], [1,6,7,6,9,1,7,1,8,6,10,2,1,10,5,8,4,8,4,10]],
               [[1],[2]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.gridGame(grid)
    print(f'r = {r}')
    print('==========================')


