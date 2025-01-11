from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        xmin = m
        ymin = n
        for a, b in ops:
            xmin = min(a, xmin)
            ymin = min(b, ymin)
        return xmin * ymin

# Main section
for m, n, ops in [
                    (3, 3, [[2,2],[3,3]]),
                    (3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]),
                    (3, 3, []),
                    (5, 6, [[3,3],[4,6],[3,3],[4,6],[4,6],[3,3]]),
                    (5, 6, [[5,1],[3,3],[2,2],[2,2]]),
                 ]:
    print(f'm = {m}, n = {n}, ops = {ops}')
    sol = Solution()
    r = sol.maxCount(m, n, ops)
    print(f'r = {r}')
    print('==========================')

