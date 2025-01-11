from typing import List

class Solution:
    def __init__(self):
        self.island_count = 0

    def flood_fill(self, grid: List[List[str]], r: int, c: int, rlen: int, clen: int) -> List[List[str]]:
        # Skip if we reached the boundaries
        if r < 0 or r >= rlen:
            return grid
        if c < 0 or c >= clen:
            return grid
        # Skip if block has water or is visited.
        if int(grid[r][c]) <= 0:
            return grid
        # Set the block as visited
        grid[r][c] = '-1'
        # Flood fill all blocks around this block, and set them as visited.
        grid = self.flood_fill(grid, r,   c-1, rlen, clen)
        grid = self.flood_fill(grid, r,   c+1, rlen, clen)
        grid = self.flood_fill(grid, r-1, c,   rlen, clen)
        grid = self.flood_fill(grid, r+1, c,   rlen, clen)
        return grid

    def numIslands(self, grid: List[List[str]]) -> int:
        # The algorithm for findings islands is simple:
        # 1) Iterate through all rows, all columns
        # 2) If a block has value '1', it has not been visited. Hence, increment island_count.
        # 3) Call flood_fill method and flood fill the neighborhood of the block as visited (value = -1).
        #    Note that passing the grid is necessary to retain the updates in the grid.
        # In this way, every "island" will be incremented only once - when we reach the
        # first block of that island.
        # Value = 0  means "water".
        # Value = 1  means "land that has not been visited".
        # Value = -1 means "land that has been visited".
        rlen = len(grid)
        clen = len(grid[0])
        for r in range(rlen):
            for c in range(clen):
                # Skip the block if it has water (0) or has been visited (-1)
                if int(grid[r][c]) <= 0:
                    continue
                # Otherwise, increase the island_count, set the block as visited
                # and flood fill its connected blocks
                if int(grid[r][c]) == 1:
                    self.island_count += 1
                    grid = self.flood_fill(grid, r, c, rlen, clen)
        return self.island_count

# Main section
for grid in [
                 [ ['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0'] ],
                 [ ['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1'] ],
                 [ ['1','1','1'], ['1','1','0'], ['1','0','1'] ],
                 [ ['1','1','0','1','1'], ['1','1','1','1','0'], ['1','1','1','1','0'], ['0','1','1','1','1'], ['1','1','1','1','1'], ['1','1','1','0','0'] ],
                 [ ['1','1','0','1','1'], ['1','1','0','1','0'], ['1','0','1','0','0'], ['0','1','0','1','1'], ['1','1','1','1','1'], ['1','1','1','0','0'] ],
                 [ ['0','0','0'], ['0','1','1'] ],
                 [ ['0'] ],
                 [ ['0', '1'] ],
                 [ ['0'], ['1'] ],
                 [ ['0', '0'], ['1', '1'] ],
                 [ ['0', '0'], ['0', '0'] ],
                 [ ['0','1','0','1','0','1'], ['1','0','1','0','1','0'], ['0','1','0','1','0','1'], ['1','0','1','0','1','0'] ],
            ]:
    sol = Solution()
    print(f'grid = {grid}')
    r = sol.numIslands(grid)
    print(f'r = {r}')
    print('==========================')


