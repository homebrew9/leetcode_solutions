from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            if nums[i] % 2 == 0:
                nums[i] = 0
            elif nums[i] % 2 == 1:
                nums[i] = 1
        nums.sort()
        return nums

# Main section
for nums in [
               [4,3,2,1],
               [1,5,1,4,2],
               [716,129,387,940,873,675,53,687,192,692,669,580,261,52,972,870,277,866,834,551,47,353,653,657,959,458,150,467,297,976],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.transformArray(nums)
    print(f'r    = {r}')
    print('================================')

