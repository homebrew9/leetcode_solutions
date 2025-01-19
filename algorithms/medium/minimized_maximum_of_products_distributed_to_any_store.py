from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def number_of_stores(max_per_store):
            res = 0
            for q in quantities:
                res += math.ceil(q / max_per_store)
            return res
        left, right = 1, 10**5
        while left <= right:
            mid = (left + right) // 2
            val = number_of_stores(mid)
            if val <= n:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Main section
for n, quantities in [
                        (6, [11,6]),
                        (7, [15,10,10]),
                        (10, [1,2,3,3,4,4,6,7,8,9]),
                        (11, [1,2,3,3,4,4,6,7,8,9]),
                        (12, [1,2,3,3,4,4,6,7,8,9]),
                        (13, [1,2,3,3,4,4,6,7,8,9]),
                        (14, [1,2,3,3,4,4,6,7,8,9]),
                        (15, [1,2,3,3,4,4,6,7,8,9]),
                        (16, [1,2,3,3,4,4,6,7,8,9]),
                        (17, [1,2,3,3,4,4,6,7,8,9]),
                        (18, [1,2,3,3,4,4,6,7,8,9]),
                        (19, [1,2,3,3,4,4,6,7,8,9]),
                        (20, [1,2,3,3,4,4,6,7,8,9]),
                     ]:
    print(f'n, quantities = {n}, {quantities}')
    sol = Solution()
    r = sol.minimizedMaximum(n, quantities)
    print(f'r = {r}')
    print('=====================')


