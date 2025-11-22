from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        seen = set(nums)
        res = list()
        for n in range(1, N + 1):
            if n not in seen:
                res.append(n)
        return res
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))

# Main section
for nums in [
               [4,3,2,7,8,2,3,1],
               [1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDisappearedNumbers(nums)
    r1 = sol.findDisappearedNumbers_1(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('===========================')



