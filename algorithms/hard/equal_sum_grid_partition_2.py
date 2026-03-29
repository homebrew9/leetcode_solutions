from typing import List
from itertools import chain

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def partitionExists(arr: List[List[int]]) -> bool:
            upleft, uprght = arr[0][0], arr[0][-1]
            sm, seen = 0, set()
            for idx, row in enumerate(arr):
                sm += sum(row)
                diff = 2*sm - gridSum
                if diff == 0:
                    return True
                seen |= set(row)
                if diff in [upleft, uprght, row[0]]:
                    return True
                if len(row) == 1 or idx == 0:
                    continue
                if diff in seen:
                    return True
            return False

        gridSum = sum(chain(*grid))
        return ( partitionExists(grid) or
                 partitionExists(grid[::-1]) or
                 partitionExists(grid:= list(zip(*grid))) or    # type: ignore
                 partitionExists(grid[::-1])
               )

# Main section
for grid in [
               [[1,4],[2,3]],
               [[1,2],[3,4]],
               [[1,2,4],[2,3,5]],
               [[4,1,8],[3,2,6]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.canPartitionGrid(grid)
    print(f'r = {r}')
    print('==================================')





