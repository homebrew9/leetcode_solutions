from typing import List
from collections import Counter, deque

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def calculate_xsum(arr):
            cntr = Counter(arr)
            lst = sorted([(k, v) for k, v in cntr.items()], key=lambda a: (-a[1], -a[0]))[:x]
            return sum([k * v for k, v in lst])
        dq = deque()
        res = list()
        for i, v in enumerate(nums):
            dq.append(v)
            if i >= k:
                dq.popleft()
            if i >= k - 1:
                res.append(calculate_xsum(list(dq)))
        return res

    def findXSum_1(self, nums: List[int], k: int, x: int) -> List[int]:
        def xsum(arr, x):
            cntr = Counter(arr)
            lst = sorted([(k, v) for k, v in cntr.items()], key=lambda x: (-x[1], -x[0]))
            ans = sum([v * f for v, f in lst[:x]])
            return ans
        N = len(nums)
        res = list()
        for i in range(0, N - k + 1):
            val = xsum(nums[i:i+k], x)
            res.append(val)
        return res

# Main section
for nums, k, x in [
                     ([1,1,2,2,3,4,2,3], 6, 2),
                     ([3,8,7,8,7,5], 2, 2),
                  ]:
    print(f'nums, k, x = {nums}, {k}, {x}')
    sol = Solution()
    r = sol.findXSum(nums, k, x)
    r1 = sol.findXSum_1(nums, k, x)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=====================')











