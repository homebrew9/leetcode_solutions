from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        '''
        Intuition:
        1) If we have two negatives spread anywhere in the matrix, then we can *ALWAYS* link
           them through a chain of transformations and set both of them as positive.
        2) If count of negatives is even, say 2n, then we fix the 2n negatives and make
           them positives as per Rule 1) above. 
        3) If count of negatives is odd, say 2n+1, then we fix the first 2n even negatives
           and make them positives as per Rule 1). But the last negative will always remain
           negative, so we should set the smallest one as negative. The "smallest one" is
           element with least absolute value. We can "transfer" the negative sign from the
           last negative number to the one with least absolute value. If the element with
           least absolute value is negative, it becomes positive (which is good). If it is
           positive, it becomes negative but the impact is minimal.
        Try out a few examples to test this intuition.
        '''
        N = len(matrix)
        total = 0
        min_abs_value = float('inf')
        negative_count = 0
        for r in range(N):
            for c in range(N):
                if matrix[r][c] < 0:
                    negative_count += 1
                min_abs_value = min(min_abs_value, abs(matrix[r][c]))
                total += abs(matrix[r][c])
        if negative_count % 2 == 1:
            total -= 2 * min_abs_value
        return total

# Main section
for matrix in [
                 [[1,-1],[-1,1]],
                 [[1,2,3],[-1,-2,-3],[1,2,3]],
                 [[-1,0,-1],[2,1,3],[3,-2,2]],
                 [[5,2,-6,4,7],[7,3,3,5,-1],[10,2,-3,-4,5],[-9,0,0,4,-2],[-9,-8,-4,4,3]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.maxMatrixSum(matrix)
    print(f'r = {r}')
    print('=====================')


