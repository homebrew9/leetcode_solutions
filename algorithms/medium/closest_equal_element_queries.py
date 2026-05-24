from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        L = len(nums)
        hsh = defaultdict(list)
        for i, v in enumerate(nums):
            hsh[v] += [i]
        N = len(queries)
        res = [-1 for _ in range(N)]
        for i, q in enumerate(queries):
            val = nums[q]
            if len(hsh[val]) > 1:
                arr = hsh[val]
                size = len(arr)
                idx = bisect.bisect_right(arr, q) - 1
                if idx == 0:
                    right = arr[1] - arr[0]
                    left = L - arr[-1] + arr[0]
                elif idx == size - 1:
                    left = arr[idx] - arr[idx-1]
                    right = L - arr[-1] + arr[0]
                else:
                    left = arr[idx] - arr[idx-1]
                    right = arr[idx+1] - arr[idx]
                res[i] = min(left, right)
        return res

# Main section
for nums, queries in [
                        ([1,3,1,4,1,3,2], [0,3,5]),
                        ([1,2,3,4], [0,1,2,3]),
                     ]:
    print(f'nums, queries = {nums}, {queries}')
    sol = Solution()
    r = sol.solveQueries(nums, queries)
    print(f'r = {r}')
    print('==================================')





