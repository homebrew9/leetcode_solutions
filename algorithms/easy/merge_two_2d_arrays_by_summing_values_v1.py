#
# A different algorithm that uses dictionaries to merge two 2D arrays. TC = O(NlogN), SC = O(N)
#
from typing import List
from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hsh = defaultdict(int)
        for x, y in nums1:
            hsh[x] += y
        for x, y in nums2:
            hsh[x] += y
        res = list()
        for k in sorted(hsh.keys()):
            res.append([k, hsh[k]])
        return res

# Main section
for nums1, nums2 in [
                       ([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]),
                       ([[2,4],[3,6],[5,5]], [[1,3],[4,3]]),
                    ]:
    print(f'nums1 = {nums1}')
    print(f'nums2 = {nums2}')
    sol = Solution()
    r = sol.mergeArrays(nums1, nums2)
    print(f'r     = {r}')
    print('================================')

