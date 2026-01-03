from typing import List
from math import isqrt
from functools import cache

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        @cache
        def get_divisor_sum(n):
            divisor_set = {1, n}
            is_valid = True
            for i in range(2, isqrt(n) + 1):
                if i not in divisor_set and n % i == 0:
                    if len(divisor_set) == 4:
                        is_valid = False
                        break
                    divisor_set.add(i)
                    divisor_set.add(n//i)
            if is_valid and len(divisor_set) == 4:
                return sum(divisor_set)
            else:
                return 0
        res = 0
        for num in nums:
            res += get_divisor_sum(num)
        return res

# Main section
for nums in [
               [21,4,7],
               [21,21],
               [1,2,3,4,5],
               [1,2,3,4,5,6,7,8,9,10],
               [98645,91932,95506,98457,95219,92232,97356,94025,91256,96516,92589,98566,99583,90947,98172,98815,98771,97991,98693,97568,90092,97402,96451,90594,95536],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.sumFourDivisors(nums)
    print(f'r = {r}')
    print('========================')







