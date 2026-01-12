from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_above(y):
            total = 0
            for x1, y1, s1 in squares:
                y1, s1 = y1 * FACTOR, s1 * FACTOR
                if y < y1:
                    total += s1 * s1
                elif y1 <= y <= (y1 + s1):
                    total += (y1 + s1 - y) * s1
            return total
        ymin, ymax, total_area = 0, -1, 0
        for x, y, s in squares:
            ymax = max(ymax, y + s)
            total_area += s * s
        FACTOR = 1000000
        total_area = total_area * FACTOR * FACTOR
        left, right = ymin * FACTOR, ymax * FACTOR
        while left <= right:
            mid = (left + right) // 2
            area1 = area_above(mid)
            if area1 <= total_area / 2:
                right = mid - 1
            else:
                left = mid + 1
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






