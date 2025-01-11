from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        curr = 0
        for n in nums:
            if n == 0:
                curr += 1
            elif curr > 0:
                cnt += (curr * (curr + 1))//2
                curr = 0
        if curr > 0:
            cnt += (curr * (curr + 1))//2
        return cnt

# Main section
for nums in [
               [1,3,0,0,2,0,0,4],
               [0,0,0,2,0,0],
               [0],
               [0,0],
               [1,2,3,0,0,0,0],
               [1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.zeroFilledSubarray(nums)
    print(f'r = {r}')
    print('===================')

