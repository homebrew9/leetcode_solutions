from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        res = list()
        for i in range(min(nums), max(nums)+1):
            if i not in nums_set:
                res.append(i)
        return res

# Main section
for nums in [
               [1,4,2,5],
               [7,8,6,9],
               [5,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findMissingElements(nums)
    print(f'r = {r}')
    print('=====================')











































