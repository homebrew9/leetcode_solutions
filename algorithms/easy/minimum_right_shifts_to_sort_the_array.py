from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        dips = 0
        pos = None
        N = len(nums)
        for i in range(1, N):
            if nums[i] < nums[i-1]:
                dips += 1
                pos = i
        if dips == 0:
            return 0
        if dips == 1 and nums[-1] < nums[0]:
            return N - pos
        return -1

# Main section
for nums in [
               [3,4,5,1,2],
               [1,3,5],
               [2,1,4],
               [1],
               [1,2],
               [2,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumRightShifts(nums)
    print(f'r = {r}')
    print('==================')

