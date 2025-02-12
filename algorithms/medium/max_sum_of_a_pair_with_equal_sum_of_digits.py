from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Intuition: Group the elements by their digit sum in a dictionary. If the dictionary values are SortedLists, then
        # the last two elements return the greatest sum. Find the max by iterating over all values that have 2 or more elements.
        def get_digit_sum(n):
            res = 0
            while n > 0:
                q, r = divmod(n, 10)
                res += r
                n = q
            return res
        hsh = defaultdict(SortedList)
        for n in nums:
            hsh[get_digit_sum(n)] += [n]
        res = -1
        for v in hsh.values():
            if len(v) >= 2:
                res = max(res, v[-1] + v[-2])
        return res

# Main section
for nums in [
               [18,43,36,13,7],
               [10,12,19,14],
               [8998,5311,7092,6571,9373,5608,9434,1417,1514,6339,215,8437,4081,2199,7825,9156,5024,1129,3224,4887,5958,1647,6923,7078,5188,2751,846,6187,2134,1807,2092,5058,8649,5395,7211,4653,3074,5479,5207,6071,5667,7088,1850,3029,6210,4339,6115,3749,7298,7135,5388,136,5505,4680,3940,7137,2365,7627,6834,4646,8380,3889,3898,6218,8671,3634,3053,5630,1371,4475,7534,6101,4969,8640,2912,2894,3582,1446,5334,7562,6280,738,5212,1386,2736,5868,6169,8098,8595,4837,8168,7338,3130,7385,8502,4567,4388,1927,5755,2908],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumSum(nums)
    print(f'r = {r}')
    print('==========================')

