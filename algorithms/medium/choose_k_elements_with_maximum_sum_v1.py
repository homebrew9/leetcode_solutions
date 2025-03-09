#
# Was almost there, but couldn't solve it during the contest. :(
# Learning 1: Do not sum a SortedList over and over again inside a loop! Maintain a "total" variable for that.
# Learning 2: Use *Min Heap* to maintain top k *largest* elements.
#             Use *Max Heap* to maintain top k *smallest* elements.
#
from typing import List
import heapq

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        h = list()
        heapq.heapify(h)
        arr = sorted([(v, i) for i, v in enumerate(nums1)])
        res = [0 for _ in range(N)]
        total = 0
        for i in range(0, N-1):
            idx = arr[i][1]
            heapq.heappush(h, nums2[idx])
            total += nums2[idx]
            if len(h) > k:
                val = heapq.heappop(h)
                total -= val
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

