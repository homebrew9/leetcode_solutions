#
# twitch_tv_qiqi_impact
#
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = [0] * value
        for x in nums:
            d[x%value] += 1
        print(f'\td = {d}')
        md = min(d)
        ret = md * value
        for i in range(value):
            if d[i] == md:
                return ret + i

# Main section
for nums, value in [
                      ([1,-10,7,13,6,8], 5),
                      ([1,-10,7,13,6,8], 7),
                      ([3,0,3,2,4,2,1,1,0,4], 5),
                   ]:
    print(f'nums, value = {nums}, {value}')
    sol = Solution()
    r = sol.findSmallestInteger(nums, value)
    print(f'r = {r}')
    print('=====================')

