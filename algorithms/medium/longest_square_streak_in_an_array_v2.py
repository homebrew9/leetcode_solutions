#
# This algorithm works. It passes all test cases!
#
from typing import List
import math
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        streaks = list()
        seen = set()
        for n in nums:
            v = math.sqrt(n)
            if v == int(v) and v in seen:
                added = False
                for i in range(len(streaks)):
                    lst = streaks[i]
                    if lst[-1] == v:
                        streaks[i].append(n)
                        added = True
                if not added:
                    streaks.append([v, n])
            seen.add(n)
        #print(streaks)
        if len(streaks) == 0:
            return -1
        res = max([len(x) for x in streaks])
        return -1 if res < 2 else res

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


