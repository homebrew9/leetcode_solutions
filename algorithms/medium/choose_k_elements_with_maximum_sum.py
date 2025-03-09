from typing import List
from sortedcontainers import SortedList

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        sl = SortedList()
        arr = sorted([(v, i) for i, v in enumerate(nums1)])
        res = [0 for _ in range(N)]
        total = 0
        for i in range(0, N-1):
            idx = arr[i][1]
            sl.add(-nums2[idx])
            total += nums2[idx]
            if len(sl) > k:
                val = sl.pop()
                total -= -val
            if arr[i+1][0] > arr[i][0]:
                res[arr[i+1][1]] = total
            else:
                res[arr[i+1][1]] = res[arr[i][1]]
        return res

# Main section
for nums1, nums2, k in [
                          ([4,2,1,5,3], [10,20,30,40,50], 2),
                          ([2,2,2,2], [3,1,2,3], 1),
                          ([18,11,24,9,10,11,7,29,16], [28,26,27,4,2,19,23,1,2], 1),
                       ]:
    print(f'nums1, nums2, k = {nums1}, {nums2}, {k}')
    sol = Solution()
    r = sol.findMaxSum(nums1, nums2, k)
    print(f'r = {r}')
    print('=========================')

