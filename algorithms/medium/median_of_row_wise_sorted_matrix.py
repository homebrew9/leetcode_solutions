#
# The first solution uses a Min Heap and is not less than O(m*n) complexity.
# The second solution uses Binary Search and has O(m * log(n)) complexity
#

import heapq
from bisect import bisect_right
from typing import List

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        median = (rows * cols + 1) // 2
        h = list()
        heapq.heapify(h)
        for r in range(rows):
            for c in range(cols):
                heapq.heappush(h, grid[r][c])
                if len(h) > median:
                    heapq.heappop(h)
        return h[0]

    def matrixMedian_1(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        median = (rows * cols + 1) // 2
        left, right = float('inf'), float('-inf')
        for r in range(rows):
            for c in range(cols):
                left = min(left, grid[r][c])
                right = max(right, grid[r][c])
        # Use binary search to come up with the best guess of
        # the median value and then determine its position in
        # the overall sorted array
        while left <= right:
            mid = (left + right) // 2
            pos = 0
            for r in range(rows):
                pos += bisect_right(grid[r], mid)
            if pos < median:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def matrixMedian_2(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        median = (rows * cols + 1) // 2
        left, right = float('inf'), float('-inf')
        for r in range(rows):
            for c in range(cols):
                left = min(left, grid[r][c])
                right = max(right, grid[r][c])
        # ==== Double Binary Search ====
        # Use binary search to come up with the best guess of
        # the median value and then determine its position in
        # the overall sorted array
        while left <= right:
            mid = (left + right) // 2
            pos = 0
            for r in range(rows):
                arr = grid[r]
                lft, rgt = 0, cols - 1
                while lft <= rgt:
                    m = (lft + rgt) // 2
                    if arr[m] <= mid:
                        lft = m + 1
                    else:
                        rgt = m - 1
                pos += lft
                #pos += bisect_right(grid[r], mid)
            if pos < median:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Main section
for grid in [
               [[1,1,2],[2,3,3],[1,3,4]],
               [[1,1,3,3,4]],
               [[1,3,3,5,6],[1,1,5,5,7],[3,3,5,6,8],[5,6,6,6,7],[1,1,3,5,6]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.matrixMedian(grid)
    print(f'r    = {r}')
    r1 = sol.matrixMedian_1(grid)
    print(f'r1   = {r1}')
    r2 = sol.matrixMedian_2(grid)
    print(f'r2   = {r2}')
    print('==================')


