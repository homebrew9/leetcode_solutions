from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dnums = list(set(nums))
        dnums.sort()
        if len(dnums) < 3:
            return dnums[-1]
        else:
            return dnums[-3]

# Main section
for nums in [
                 [3,2,1],
                 [1,2],
                 [2,2,3,1],
                 [2,2,3,1,9,7,5],
                 [1,2,3,4,5,6,7,8,9],
                 [9,8,7,6,5,4,3,2,1],
                 [0],
                 [-1,1],
                 [-5,-4,-3,-2,-1],
                 [-1,-2,-3,-4,-5,-5,-5,-5],
                 [2,2,3,3,5,5,4,4,0,-6,0],
                 [2,2,7,7,9,9,4,4,0,-6,0],
            ]:
    sol = Solution()
    print(f'nums = {nums}')
    r = sol.thirdMax(nums)
    print(f'r = {r}')
    print('==========================')

