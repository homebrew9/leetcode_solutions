from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)

        # lpfx[i] = max value in index range [0, i], both inclusive
        lpfx = [None for _ in range(N)]
        for i in range(N):
            lpfx[i] = nums[i] if i == 0 else max(lpfx[i-1], nums[i])

        # rpfx[i] = max value in index range [i, N-1], both inclusive
        rpfx = [None for _ in range(N)]
        for i in range(N-1, -1, -1):
            rpfx[i] = nums[i] if i == N-1 else max(rpfx[i+1], nums[i])

        res = 0
        for i in range(1, N-1):
            res = max(res, (lpfx[i-1] - nums[i]) * rpfx[i+1])
        return res
 
# Main section
for nums in [
               [12,6,1,2,7],
               [1,10,3,4,19],
               [1,2,3],
               [16,48,67,18,25,65,75,1,48,20,83,6,27,30,60,51,75,63,46,85,76,10,45,99,4,66,60,7,61,28],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumTripletValue(nums)
    print(f'r = {r}')
    print('======================')

       