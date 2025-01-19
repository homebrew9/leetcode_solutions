from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] != nums[i+1]:
                res += 1
        return res

# Main section
for nums in [
               [1,4,2],
               [10,10,10],
               [9,0,0,0,10,5,4],
               [9,0,7,0,10,5,4],
               [9,0,7,0,10,4,4],
               [9,3,7,0,10,4,4],
               [9,7,7,0,10,4,4],
               [9,4,7,0,10,4,4],
               [9,5,7,0,10,4,4],
               [9,5,10,4,4,10],
               [9,5,4,5,4,10],
               [4,9,4,5,4,10],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r = {r}')
    print('==================')


