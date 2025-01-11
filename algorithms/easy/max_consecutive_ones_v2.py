from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(i) for i in ''.join([str(i) for i in nums]).split('0')])

# Main section
for nums in [
               [1,1,0,1,1,1],
               [1,0,1,1,0,1],
               [0,0,0,0,1,0,0,1,1,1],
               [1],
               [1,1,1,1],
               [0,0,0,0,0],
               [0],
            ]:
    sol = Solution()
    print(f'nums = {nums}')
    r = sol.findMaxConsecutiveOnes(nums)
    print(f'r = {r}')
    print('==========================')



