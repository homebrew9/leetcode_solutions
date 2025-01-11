from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # We can compare slopes of each point against the origin (P0)
        # Slope(p0, p1) = slope(p0, p2)
        # => (y1-y0)/(x1-x0) = (y2-y0)/(x2-x0)
        # => (y1-y0)*(x2-x0) = (y2-y0)*(x1-x0)
        # => dy * (x2-x0) = (y2-y0) * dx, where dx = x1-x0, dy = y1-y0
        # Get dx and dy first. Then for each point from index 2 onwards, get
        # (xi-x0) and (yi-y0) and test the equality above.
        def getxdiff(arr1, arr2):
            return arr2[0] - arr1[0]
        def getydiff(arr1, arr2):
            return arr2[1] - arr1[1]

        origin = coordinates[0]
        dx = getxdiff(coordinates[1], origin)
        dy = getydiff(coordinates[1], origin)

        for p in coordinates[2:]:
            xdel = getxdiff(p, origin)
            ydel = getydiff(p, origin)
            if dy * xdel != ydel * dx:
                return False
        return True

# Main section
for coordinates in [
                      [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
                      [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],
                      [[0,0],[0,1],[0,-1]],
                      [[2,4],[2,5],[2,8]],
                      [[1,1],[2,2],[2,0]],
                   ]:
    print(f'coordinates = {coordinates}')
    sol = Solution()
    r = sol.checkStraightLine(coordinates)
    print(f'r = {r}')
    print('===================')

