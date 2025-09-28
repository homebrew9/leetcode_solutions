from typing import List
import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def get_distance(x1, y1, x2, y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        def can_form_triangle(a, b, c):
            if a == 0 or b == 0 or c == 0:
                return False
            return a + b > c and a + c > b and b + c > a
        def get_triangle_area(a, b, c):
            # We can use Heron's formula for triangle area
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        N = len(points)
        res = 0
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                for k in range(j + 1, N):
                    x3, y3 = points[k]
                    a = get_distance(x1, y1, x2, y2)
                    b = get_distance(x2, y2, x3, y3)
                    c = get_distance(x1, y1, x3, y3)
                    if can_form_triangle(a, b, c):
                        area = get_triangle_area(a, b, c)
                        res = max(res, area)
        return round(res, 6)

# Main section
for points in [
                 [[0,0],[0,1],[1,0],[0,2],[2,0]],
                 [[1,0],[0,0],[0,1]],
                 [[2,-12],[-20,46],[-16,5],[-13,-18],[27,-31],[7,48],[17,6],[-42,25],[-49,3],[17,-41]],
                 [[10,-15],[26,5],[-44,-11],[49,22],[22,16],[-29,20],[37,-35],[-44,-6],[23,14],[12,-47],[50,-1],[-26,-22],[40,39],[3,26],[-41,29],[-16,46],[28,-36],[-31,-43],[2,-34],[12,-2]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.largestTriangleArea(points)
    print(f'r = {r}')
    print('=============')






