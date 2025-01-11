from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        pts1 = [(i,j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        pts2 = [(i,j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        counter = Counter((x1 - x2, y1 - y2) for x1, y1 in pts1 for x2,y2 in pts2)
        print(Counter((x1 - x2, y1 - y2) for x1, y1 in pts1 for x2,y2 in pts2))
        return max(counter.values() or [0])

# Main section
for img1, img2 in [
                     #([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]),
                     #([[1,1,0,1,0],[0,1,0,0,1],[0,1,0,1,0],[1,1,0,1,0],[0,0,1,1,1]], [[1,1,0,0,0],[0,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,1,1]]),
                     #([[0,0,0,1,1],[0,1,0,0,1],[1,1,0,0,0],[1,0,1,0,1],[0,1,0,1,0]], [[0,1,0,1,0],[1,1,0,1,0],[1,0,1,0,0],[1,1,1,0,0],[0,0,0,1,1]]),
                     ([[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]),
                  ]:
    print(f'imag1, img2 = {img1}, {img2}')
    sol = Solution()
    r = sol.largestOverlap(img1, img2)
    print(f'r = {r}')
    print('====================')

