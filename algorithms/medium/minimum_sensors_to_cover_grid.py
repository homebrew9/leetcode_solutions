import math

class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        # Each sensor has a coverage of 2k + 1. We simply lay down
        # sensors in a rectangular fashion inside the grid
        # i.e. left to right from top to bottom ensuring that
        # each sensor covers its max area.
        # Draw it with pen / paper to visualize it better.
        coverage = 2*k + 1
        row_sensors = math.ceil(n / coverage)
        col_sensors = math.ceil(m / coverage)
        return row_sensors * col_sensors
 
# Main section
for n, m, k in [
                  (5, 5, 1),
                  (2, 2, 2),
                  (1000, 1000, 1),
                  (863, 571, 131),
               ]:
    print(f'n, m, k = {n}, {m}, {k}')
    sol = Solution()
    r = sol.minSensors(n, m, k)
    print(f'r = {r}')
    print('===================')

























