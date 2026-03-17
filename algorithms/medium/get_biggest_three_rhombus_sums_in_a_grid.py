from typing import List
import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def is_within_bounds(r, c, n):
            if n == 0:
                return True
            return 0 <= r + n < rows and 0 <= c + n < cols and \
                   0 <= c - n < cols and 0 <= r + 2*n < rows
        def get_rhombus_sum(r, c, n):
            if n == 0:
                return grid[r][c]
            res = grid[r][c] + grid[r+2*n][c]
            for d in range(1, 2*n):
                if d <= n:
                    res += grid[r+d][c-d] + grid[r+d][c+d]
                else:
                    res += grid[r+d][c-2*n+d] + grid[r+d][c+2*n-d]
            return res
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        h = list()
        heapq.heapify(h)
        res = 0
        for r in range(rows):
            for c in range(cols):
                n = 0
                while is_within_bounds(r, c, n):
                    res = get_rhombus_sum(r, c, n)
                    if res not in seen:
                        seen.add(res)
                        heapq.heappush(h, res)
                        if len(h) > 3:
                            heapq.heappop(h)
                    n += 1
        return sorted(h, reverse=True)
    def getBiggestThree_1(self, grid: List[List[int]]) -> List[int]:
        def is_within_bounds(r, c, n):
            if n == 0:
                return True
            return 0 <= r + n < rows and 0 <= c + n < cols and \
                   0 <= c - n < cols and 0 <= r + 2*n < rows
        def get_rhombus_sum(r, c, n):
            if n == 0:
                return grid[r][c]
            res = grid[r][c] + grid[r+n][c+n] + grid[r+n][c-n] + grid[r+2*n][c]
            r1, c1 = r + 1, c + 1
            while r1 < r + n and c1 < c + n:
                res += grid[r1][c1]
                r1, c1 = r1 + 1, c1 + 1
            r1, c1 = r + 1, c - 1
            while r1 < r + n and c1 > c - n:
                res += grid[r1][c1]
                r1, c1 = r1 + 1, c1 - 1
            r1, c1 = r + n + 1, c + n - 1
            while r1 < r+2*n and c1 > c:
                res += grid[r1][c1]
                r1, c1 = r1 + 1, c1 - 1
            r1, c1 = r + n + 1, c - n + 1
            while r1 < r+2*n and c1 < c:
                res += grid[r1][c1]
                r1, c1 = r1 + 1, c1 + 1
            return res
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        h = list()
        heapq.heapify(h)
        res = 0
        for r in range(rows):
            for c in range(cols):
                n = 0
                while is_within_bounds(r, c, n):
                    res = get_rhombus_sum(r, c, n)
                    if res not in seen:
                        seen.add(res)
                        heapq.heappush(h, res)
                        if len(h) > 3:
                            heapq.heappop(h)
                    n += 1
        return sorted(h, reverse=True)

# Main section
for grid in [
               [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]],
               [[1,2,3],[4,5,6],[7,8,9]],
               [[7,7,7]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.getBiggestThree(grid)
    r1 = sol.getBiggestThree_1(grid)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===============================')







