from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Using math formulas.
        # Sum of positive integers: 1 + 2 + ... + n = n * (n+1) // 2
        # Sum of squares of positive integers: 1^2 + 2^2 + ... + n^2 = n * (n+1) * (2*n + 1) // 6
        #
        N = len(grid)
        perfectSum = N*N * (N*N + 1) // 2
        perfectSumSq = N*N * (N*N + 1) * (2*N*N + 1) // 6
        candSum = sum([elem for lst in grid for elem in lst])
        candSumSq = sum([elem*elem for lst in grid for elem in lst])
        sumDiff = candSum - perfectSum
        sumSqrDiff = candSumSq - perfectSumSq
        x = ((sumSqrDiff // sumDiff) + sumDiff) // 2
        y = ((sumSqrDiff // sumDiff) - sumDiff) // 2
        return [x, y]

# Main section
for grid in [
               [[1,3],[2,2]],
               [[9,1,7],[8,9,2],[3,4,6]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.findMissingAndRepeatedValues(grid)
    print(f'r = {r}')
    print('================================')

