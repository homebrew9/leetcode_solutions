from typing import List
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Use math.log10() to determine the number of digits
        return sum([(math.floor(math.log10(x)) + 1) % 2 == 0 for x in nums])

    def findNumbers_1(self, nums: List[int]) -> int:
        return sum([9 < x < 100 or 999 < x < 10000 or x == 100_000 for x in nums])

    def findNumbers_2(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            digits = 0
            while n > 0:
                p, q = divmod(n, 10)
                digits += 1
                n = p
            res += digits%2 == 0
        return res

    def findNumbers_3(self, nums: List[int]) -> int:
        return sum([len(list(str(i)))%2==0 for i in nums])

# Main section
for nums in [
               [12,345,2,6,7896],
               [555,901,482,1771],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findNumbers(nums)
    r1 = sol.findNumbers_1(nums)
    r2 = sol.findNumbers_2(nums)
    r3 = sol.findNumbers_3(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r3 = {r3}')
    print('==================')

