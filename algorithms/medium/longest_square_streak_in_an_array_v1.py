#
# Throws WA for Testcase # 1 and 6. Output for TC # 1 = 2, it should be 3. Output for TC # 6 = 4, it should be 3.
#
from typing import List
import math

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        hsh = dict()
        for i, v in enumerate(nums):
            n = v
            while math.sqrt(n) == int(math.sqrt(n)):
                n = int(math.sqrt(n))
                if not n in hsh:
                    break
            if n in hsh:
                hsh[n] += [v]
            else:
                hsh[n] = [v]
        print(f'\thsh = {hsh}')
        longest_streak = 0
        for k, v in hsh.items():
            if len(set(v)) > longest_streak:
                #print(f'\t\tk, v = {k}, {v}')
                longest_streak = len(set(v))
        if longest_streak < 2:
            return -1
        else:
            return longest_streak

# Main section
for nums in [
               [4,3,6,16,8,2],
               [2,3,5,6,7],
               [2,91,109,3,4,4,98,786,1000,2000,9,3435,8874,81,999,2023,6561,9,3,67,78],
               [10,2,13,16,8,9,13],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestSquareStreak(nums)
    print(f'r = {r}')
    print('=======================')


