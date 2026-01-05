from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs = 0
        min_abs = 10**20
        neg_count = 0
        has_zero = False

        for row in matrix:
            for x in row:
                if x == 0:
                    has_zero = True
                total_abs += abs(x)
                min_abs = min(min_abs, abs(x))
                if x < 0:
                    neg_count += 1

        # If there's a zero or even number of negatives, all can be positive
        if has_zero or neg_count % 2 == 0:
            return total_abs
        else:
            # Odd negatives and no zero: subtract twice the smallest absolute value
            return total_abs - 2 * min_abs

# Main section
for matrix in [
                 [[1,-1],[-1,1]],
                 [[1,2,3],[-1,-2,-3],[1,2,3]],
                 [[-1,0,-1],[-2,1,3],[3,2,2]],
                 [[1,2,3],[4,5,6],[-1,-2,-3]],
                 [[10,20,30],[40,50,60],[-1,-2,-3]],
                 [[-1,0,-1],[-2,1,3],[3,0,2]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.maxMatrixSum(matrix)
    print(f'r = {r}')
    print('========================')









