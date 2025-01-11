#
# Does not work for the last test case!
#
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def minTime(x0, y0, x1, y1):
            # Are the points on a horizontal line?
            if y0 == y1:
                return abs(x0 - x1)
            # Are the points on a vertical line?
            if x0 == y1:
                return abs(y0 - y1)
            # Are the points on a line with 45 degree slope?
            if abs(y1 - y0) == abs(x1 - x0):
                return abs(y1 - y0)
            # For all other cases, we split the walk into two stages.
            # Walk diagonally to the nearest point first, and then 
            # either vertically or horizontally to the destination.
            if abs(x1 - x0) < abs(y1 - y0):
                xdelta = x1 - x0
                if abs(y1 - (y0 + xdelta)) < abs(y1 - (y0 - xdelta)):
                    ydelta = xdelta
                else:
                    ydelta = -xdelta
            elif abs(y1 - y0) < abs(x1 - x0):
                ydelta = y1 - y0
                if abs(x1 - (x0 + ydelta)) < abs(x1 - (x0 - ydelta)):
                    xdelta = ydelta
                else:
                    xdelta = -ydelta
            temp = [x0 + xdelta, y0 + ydelta]
            time_taken = abs(xdelta)
            print(f'\tFrom [{x0}, {y0}] to {temp} => time_taken = {time_taken}')
            if temp[1] == y1:
                time_taken += abs(temp[0] - x1)
            elif temp[0] == x1:
                time_taken += abs(temp[1] - y1)
            print(f'\ttime_taken till dest = {time_taken}')
            print('=======')
            return time_taken

        total_time = 0
        for i in range(1, len(points)):
            pt1 = points[i-1]
            pt2 = points[i]
            total_time += minTime(pt1[0], pt1[1], pt2[0], pt2[1])
        return total_time

# Main section
for points in [
                 [[1,1],[3,4],[-1,0]],
                 [[3,2],[-2,2]],
                 [[257,-831],[238,98],[-364,238],[646,-932],[-899,714]],
                 [[25,-83],[23,9],[-36,23],[64,-93],[-89,71]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.minTimeToVisitAllPoints(points)
    print(f'r = {r}')
    print('=======================')

