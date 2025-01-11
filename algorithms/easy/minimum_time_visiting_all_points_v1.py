from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x1, y1 = points.pop()
        print(f'\t(x1, y1) = ({x1}, {y1})')
        while points:
            x2, y2 = points.pop()
            res += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2
            print(f'\t\t(x2, y2), res = ({x2}, {y2}), {res}')
        print(f'\t(x2, y2), res = ({x2}, {y2}), {res}')
        return res

# Main section
for points in [
                 [[1,1],[3,4],[-1,0]],
                 [[3,2],[-2,2]],
                 [[257,-831],[238,98],[-364,238],[646,-932],[-899,714]],
                 [[25,-83],[23,9],[-36,23],[64,-93],[-89,71]],
                 [[3,-5],[1,1]],
                 [[-3,-4],[1,1]],
                 [[-3,2],[1,1]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.minTimeToVisitAllPoints(points)
    print(f'r = {r}')
    print('=======================')

