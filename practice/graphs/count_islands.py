#
# Given a grid where 1 is land and 0 is water, count the number of islands surrounded completely by water.
# If an island is on the edge, it has water to its side.
#
def countIslands(grid):
    def dfs(r, c):
        global total
        if visited[r][c]:
            return
        if grid[r][c] == 1:
            total -= 1
        visited[r][c] = True
        for dr, dc in directions:
            if 0 <= r+dr < rows-1 and 0 <= c+dc < cols-1 and grid[r+dr][c+dc] == 1:
                dfs(r+dr, c+dc)
    global total
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0,-1), (0,1), (-1,0), (1,0)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                total += 1
    # Iterate through the perimeter and perform dfs if any
    # cell is 1, decrementing total for each cell that is 1.
    for c in range(cols):
        # First Row
        if grid[0][c] == 1:
            dfs(0, c)
        # Last Row
        if grid[rows-1][c] == 1:
            dfs(rows-1, c)
    for r in range(1, rows-1):
        # First Column
        if grid[r][0] == 1:
            dfs(r, 0)
        # Last Column
        if grid[r][cols-1] == 1:
            dfs(r, cols-1)
    return total


for grid in [
               [[1,0,0,0,0],[0,1,0,1,0],[0,1,0,1,0],[0,0,0,0,0]],
               [[1,0,0,0],[0,1,0,0],[0,1,0,0],[1,1,1,0],[0,0,0,0]],
               [[0,0,0,0,0,0,0,0],[1,1,1,0,1,1,1,0],[0,0,1,0,0,0,0,0]],
            ]:
    print(f'grid = {grid}')
    r = countIslands(grid)
    print(f'r = {r}')
    print('=======================')


