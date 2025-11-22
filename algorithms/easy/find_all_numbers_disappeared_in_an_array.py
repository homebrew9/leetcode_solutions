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

# Main section
for nums in [
               [4,3,2,7,8,2,3,1],
               [1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDisappearedNumbers(nums)
    print(f'r = {r}')
    print('===========================')

