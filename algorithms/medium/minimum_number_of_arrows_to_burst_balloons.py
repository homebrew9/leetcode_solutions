from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        shots = 1
        overlap = points[0]
        for i in range(1, len(points)):
            a, b = overlap
            c, d = points[i]
            if max(a, c) <= min(b, d):
                overlap = [max(a, c), min(b, d)]
            else:
                shots += 1
                overlap = points[i]
        return shots

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

