#
# Beautiful solution by user: linfq
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/1686627/C%2B%2BJavaPython-6-Lines-oror-Sort-and-Greedy-oror-Image-Explanation
#
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points by their y co-ordinates. Then pass an arrow
        # from the first y-coordinate, iterate through the points and
        # check if the x-coordinate is less than the arrow mark.
        points.sort(key=lambda x: x[1])
        ans, arrow = 0, 0
        for start, end in points:
            if ans == 0 or start > arrow:
                ans += 1
                arrow = end
        return ans

# Main section
for points in [
                 [[10,16],[2,8],[1,6],[7,12]],
                 [[1,2],[3,4],[5,6],[7,8]],
                 [[1,2],[2,3],[3,4],[4,5]],
                 [[1,6],[3,9],[4,8],[10,12],[11,13]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.findMinArrowShots(points)
    print(f'r = {r}')
    print('===============')


