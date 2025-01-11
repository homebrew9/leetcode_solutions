from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        print(f'\tnums = {nums}')

        for i in range(len(nums)):
            if nums[i] > nums[ans]:
                ans += 1

        return ans

# Main section
for nums in [
               [1,3,5,2,1,3,1],
               [1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximizeGreatness(nums)
    print(f'r = {r}')
    print('===================')

