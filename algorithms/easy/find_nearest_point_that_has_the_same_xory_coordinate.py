from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        min_dist = float('inf')
        min_ind = float('inf')
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                md = manhattan_distance([x,y], point)
                if md < min_dist:
                    min_dist = md
                    min_ind = i
            #print(f'point = {point}, min_dist = {min_dist}, min_ind = {min_ind}')

        if min_ind == float('inf'):
            return -1
        else:
            return min_ind

# Main section
for x, y, points in [
                       (3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]),
                       (3,4,[[3,4]]),
                       (3,4,[[2,3]]),
                    ]:
    print(f'x, y, points = {x}, {y}, {points}')
    sol = Solution()
    r = sol.nearestValidPoint(x, y, points)
    print(f'r = {r}')
    print('=============================')

