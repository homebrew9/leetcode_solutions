from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        stack = list()
        third = float('-inf')
        for i in range(N-1, -1, -1):
            if nums[i] < third:
                return True
            while stack and stack[-1] < nums[i]:
                third = stack.pop()
            stack.append(nums[i])
        return False

# Main section
for nums in [
               [1,2,3,4],
               [3,1,4,2],
               [-1,3,2,0],
               [3,5,1,0],
               [3,5,3,3],
               [3,5,3,3,4],
               [3,5,3,3,6,3,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.find132pattern(nums)
    print(f'r = {r}')
    print('================')

