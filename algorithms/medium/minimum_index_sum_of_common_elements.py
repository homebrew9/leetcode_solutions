from typing import List
from collections import defaultdict

class Solution:
   def minimumSum(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        hsh = defaultdict(int)
        for i, v in enumerate(nums1):
            if v not in hsh:
                hsh[v] = i
        res = 10**20
        for i, v in enumerate(nums2):
            if v in hsh:
                res = min(res, i + hsh[v])
        return -1 if res == 10**20 else res

# Main section
for nums1, nums2 in [
                       ([3,2,1], [1,3,1]),
                       ([5,1,2], [2,1,3]),
                       ([6,4], [7,8]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.minimumSum(nums1, nums2)
    print(f'r = {r}')
    print('=====================')













