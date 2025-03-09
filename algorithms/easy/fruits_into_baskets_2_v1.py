# Another logic that does not involve deleting array elements.
# It's still O(N^2) but the constraints are very small: 1 <= N <= 100.
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        res = 0
        arr = [[v, i, 0] for i, v in enumerate(baskets)]
        for i in range(N):
            f = fruits[i]
            j = 0
            while j < N:
                if arr[j][0] >= f and arr[j][2] == 0:
                    arr[j][2] = 1
                    break
                j += 1
            if j >= N:
                res += 1
        return res

# Main section
for fruits, baskets in [
                          ([4,2,5], [3,5,4]),
                          ([3,6,1], [6,4,7]),
                       ]:
    print(f'fruits, baskets = {fruits}, {baskets}')
    sol = Solution()
    r = sol.numOfUnplacedFruits(fruits, baskets)
    print(f'r = {r}')
    print('=========================')

