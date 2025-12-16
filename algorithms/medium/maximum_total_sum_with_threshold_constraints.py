from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
        hsh = defaultdict(list)
        for t, n in zip(threshold, nums):
            if t not in hsh:
                hsh[t] = [1, n]
            else:
                hsh[t] = [hsh[t][0] + 1, hsh[t][1] + n]
        step = 1
        res = 0
        for k in sorted(hsh):
            if step < k:
                break
            res += hsh[k][1]
            step += hsh[k][0]
        return res

# Main section
for nums, threshold in [
                          ([1,10,4,2,1,6], [5,1,5,5,2,2]),
                          ([4,1,5,2,3], [3,3,2,3,3]),
                          ([2,6,10,13], [2,1,1,1]),
                       ]:
    print(f'nums, threshold = {nums}, {threshold}')
    sol = Solution()
    r = sol.maxSum(nums, threshold)
    print(f'r = {r}')
    print('===========================')

