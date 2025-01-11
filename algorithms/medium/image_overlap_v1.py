#
# This algorithm is incorrect! It does not work for the last test case.
# The answer for that test case is 1 but this algorithm returns 0.
#
from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Each cell in img2 can have nine translations to surrounding cells and itself. For each
        # cell in img2 with value = 1, we test all translations and see if the resulting cell in
        # img1 has value = 1. The highest frequency of any translation is the largest overlap.
        n = len(img1)
        hsh = { (-1,-1): 0, (-1,0): 0, (-1,1): 0,  # a row above
                (0,-1): 0, (0,0): 0, (0,1): 0,     # current row
                (1,-1): 0, (1,0): 0, (1,1): 0      # a row below
              }
        for r in range(n):
            for c in range(n):
                if img2[r][c] == 1:
                    for x, y in hsh:
                        if 0 <= r+x < n and 0 <= c+y < n and img1[r+x][c+y] == 1:
                            hsh[(x,y)] += 1
        return max(hsh.values())

# Main section
for img1, img2 in [
                     ([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]),
                     ([[1,1,0,1,0],[0,1,0,0,1],[0,1,0,1,0],[1,1,0,1,0],[0,0,1,1,1]], [[1,1,0,0,0],[0,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,1,1]]),
                     ([[0,0,0,1,1],[0,1,0,0,1],[1,1,0,0,0],[1,0,1,0,1],[0,1,0,1,0]], [[0,1,0,1,0],[1,1,0,1,0],[1,0,1,0,0],[1,1,1,0,0],[0,0,0,1,1]]),
                     ([[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]),
                  ]:
    print(f'imag1, img2 = {img1}, {img2}')
    sol = Solution()
    r = sol.largestOverlap(img1, img2)
    print(f'r = {r}')
    print('====================')

