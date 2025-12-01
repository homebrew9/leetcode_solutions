from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        res = list()
        for n in nums:
            x = (x * 2 + n) % 5
            res.append(x == 0)
        return res

# Main section
for nums in [
               [0,1,1],
               [1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.prefixesDivBy5(nums)
    print(f'r = {r}')
    print('===========================')



