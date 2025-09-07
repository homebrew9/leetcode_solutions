from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hsh = defaultdict(list)
        rows = len(nums)
        for r in range(rows):
            for c, v in enumerate(nums[r]):
                hsh[r+c] += [v]
        res = list()
        for k, v in sorted(hsh.items()):
            res.extend(v[::-1])
        return res

# Main section
for nums in [
               [[1,2,3],[4,5,6],[7,8,9]],
               [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]],
               [[14,12,19,16,9],[13,14,15,8,11],[11,13,1]],
               [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[31]],
               [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]],
               [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1,2,3,4,5]],
               [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1,2,3,4,5,6,7,8,9,10]],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDiagonalOrder(nums)
    print(f'r = {r}')
    print('==================')

