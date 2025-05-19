from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if not(a + b > c and b + c > a and c + a > b):
            return 'none'
        if a == b == c:
            return 'equilateral'
        if a == b or b == c or c == a:
            return 'isosceles'
        return 'scalene'

# Main section
for nums in [
               [3,3,3],
               [3,4,5],
               [4,5,5],
               [17,19,36],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.triangleType(nums)
    print(f'r    = {r}')
    print('============================')


