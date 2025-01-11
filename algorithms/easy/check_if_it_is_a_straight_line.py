from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        if x1 == x0:
            slope = float('inf')
        else:
            slope = (y1-y0)/(x1-x0)
            
        for i in range(1, len(coordinates)-1):
            x0, y0 = coordinates[i]
            x1, y1 = coordinates[i+1]
            if x1 == x0:
                curr_slope = float('inf')
            else:
                curr_slope = (y1-y0)/(x1-x0)
            if curr_slope != slope:
                return False
        return True

# Main section
for coordinates in [
                      [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
                      [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],
                      [[0,0],[0,1],[0,-1]],
                   ]:
    print(f'coordinates = {coordinates}')
    sol = Solution()
    r = sol.checkStraightLine(coordinates)
    print(f'r = {r}')
    print('===================')

