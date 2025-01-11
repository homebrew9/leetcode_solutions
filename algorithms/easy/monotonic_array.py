from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        trend = None
        for i in range(1,len(nums)):
            #print(f'\ti, nums[i], trend = {i}, {nums[i]}, {trend}')
            if nums[i] > nums[i-1]:
                if trend is None:
                    trend = 'inc'
                elif trend == 'dec':
                    return False
            elif nums[i] < nums[i-1]:
                if trend is None:
                    trend = 'dec'
                elif trend == 'inc':
                    return False
        return True

# Main section
for nums in [
               [1,2,2,3],
               [6,5,4,4],
               [1,3,2],
               [1,1,1,1,1,1],
               [1,1,1,1,1,2],
               [5,1,1,1,1,1],
               [7,1,1,1,1,2],
               [0,1,1,1,1,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isMonotonic(nums)
    print(f'r = {r}')
    print('==========================')

