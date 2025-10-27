from typing import List
from collections import defaultdict, Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = Counter(nums)                   # solution 1: line sweep, TC = O(nlogn)
        presum = defaultdict(int)
        for x in count:                         # line sweep
            presum[x-k] += count[x]
            presum[x+k+1] -= count[x]
        keys = sorted(presum.keys() | count.keys())     # search all possible keys
        ans, total = 0, 0
        for x in keys:
            total += presum[x]                          # maximum frequency for x
            ops = min(total-count[x], numOperations)    # number of operations bounded by numOperations
            ans = max(ans, count[x] + ops)              # update ans
        return ans

# Main section
for nums, k, numOperations in [
                                 ([1,4,5], 1, 2),
                                 ([5,11,20,20], 5, 1),
                                 ([88,53], 27, 2),
                                 ([2,3,4,5,5,9,9,9,9,10,10], 2, 2),
                                 ([999999997,999999999,999999999], 999999999, 2),
                              ]:
    print(f'nums, k, numOperations = {nums}, {k}, {numOperations}')
    sol = Solution()
    r = sol.maxFrequency(nums, k, numOperations)
    print(f'r = {r}')
    print('=====================')














