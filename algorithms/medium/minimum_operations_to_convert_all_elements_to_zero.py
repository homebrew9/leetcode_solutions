from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res

# Main section
for nums in [
               [0,2],
               [3,1,2,1],
               [1,2,1,2,1,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r = {r}')
    print('=====================')







