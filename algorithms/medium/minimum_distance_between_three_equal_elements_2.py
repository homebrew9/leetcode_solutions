from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # nums = [1, 1, 2, 3, 2, 1, 2]
        # 1 => [0, 1, 5] => (1-0) + (5-1) + (5-0) = 2*(5 - 0)
        # 2 => [2, 4, 6] => (4-2) + (6-4) + (6-2) = 2*(6 - 2)
        MAX = 10**20
        res = MAX
        hsh = defaultdict(list)
        for i, v in enumerate(nums):
            if len(hsh[v]) == 2:
                a, b = hsh[v]
                res = min(res, 2 * (i - a))
                hsh[v] = [b, i]
            else:
                hsh[v] += [i]
        return -1 if res == MAX else res

# Main section
for nums in [
               [1,2,1,1,3],
               [1,1,2,3,2,1,2],
               [1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumDistance(nums)
    print(f'r = {r}')
    print('=====================')




