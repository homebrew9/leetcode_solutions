from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        N = len(nums)
        changes = 0
        trend = None
        for i in range(1, N):
            if nums[i] == nums[i - 1]:
                return False
            if i == 1:
                if nums[i] < nums[i - 1]:
                    return False
                changes += 1
                trend = 'I'
            elif nums[i] < nums[i - 1]:
                if trend == 'I':
                    trend = 'D'
                    changes += 1
            elif nums[i] > nums[i - 1]:
                if trend == 'D':
                    trend = 'I'
                    changes += 1
            if changes > 3:
                return False
        return changes == 3

# Main section
for nums in [
               [1,3,5,4,2,6],
               [2,1,3],
               [1,2,3],
               [1,2,3,4,3,2,1,2,3,4,5],
               [1,2,3,4,3,3,1,2,3,4,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isTrionic(nums)
    print(f'r = {r}')
    print('==============================')



