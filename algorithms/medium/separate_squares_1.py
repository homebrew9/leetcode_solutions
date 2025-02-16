from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # The intuition is to use Binary Search. But since the solution could be a floating-point number
        # that has up to 5 decimal places, I divided each unit of the Cartesian plane into FACTOR (=10**6) 
        # pieces. The final value is divided by FACTOR before being returned.
        def total_area_below(mid):
            res = 0
            for x, y, length in squares:
                ymin = y * FACTOR
                ymax = (y + length) * FACTOR
                if mid < ymin:
                    res += 0
                elif mid > ymax:
                    res += (ymax - ymin) * length * FACTOR
                else:
                    ybelow = (mid - ymin)
                    res += ybelow * length * FACTOR
            return res
        def total_area_above(mid):
            res = 0
            for x, y, length in squares:
                ymin = y * FACTOR
                ymax = (y + length) * FACTOR
                if mid < ymin:
                    res += (ymax - ymin) * length * FACTOR
                elif mid > ymax:
                    res += 0
                else:
                    yabove = (ymax - mid)
                    res += yabove * length * FACTOR
            return res
        FACTOR = 1000000
        left, right = float('inf'), float('-inf')
        for x, y, length in squares:
            left = min(left, y)
            right = max(right, y + length)
        left = left * FACTOR
        right = right * FACTOR
        while left <= right:
            mid = (left + right) // 2
            below_area = total_area_below(mid)
            above_area = total_area_above(mid)
            if above_area > below_area:
                left = mid + 1
            else:
                right = mid - 1
        return left/FACTOR

# Main section
for squares in [
                  [[0,0,1],[2,2,1]],
                  [[0,0,2],[1,1,1]],
                  [[2,5,3],[8,12,4]],
               ]:
    print(f'squares = {squares}')
    sol = Solution()
    r = sol.separateSquares(squares)
    print(f'r = {r}')
    print('==========================')

