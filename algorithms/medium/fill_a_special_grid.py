from typing import List

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def solve(r, c, side):
            if side == 1:
                grid[r][c] = self.res
                self.res += 1
                return
            solve(r, c + side//2, side//2)
            solve(r + side//2, c + side//2, side//2)
            solve(r + side//2, c, side//2)
            solve(r, c, side//2)
        rows = 2**n
        cols = 2**n
        grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.res = 0
        solve(0, 0, 2**n)
        return grid
 
# Main section
for n in [
            0, 1, 2, 3, 4, 5,
            #6, 7, 8, 9, 10,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.specialGrid(n)
    print(f'r = {r}')
    print('============================')







