#
# Memoized versions using a custom dictionary and functools.cache decorator
#
from typing import List
from functools import cache
import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def solve(i, j):
            if i >= N:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            next_day = days[i] + day_pass[j] - 1
            idx = bisect.bisect_right(days, next_day)
            tmp = float('inf')
            for k in range(3):
                tmp = min(tmp, solve(idx, k))
            memo[(i, j)] = costs[j] + tmp
            return memo[(i, j)]
        N = len(days)
        day_pass = [1, 7, 30]
        memo = dict()
        res = min(solve(0,0), solve(0,1), solve(0,2))
        return res
    def mincostTickets_1(self, days: List[int], costs: List[int]) -> int:
        @cache
        def solve(i, j):
            if i >= N:
                return 0
            next_day = days[i] + day_pass[j] - 1
            idx = bisect.bisect_right(days, next_day)
            tmp = float('inf')
            for k in range(3):
                tmp = min(tmp, solve(idx, k))
            return costs[j] + tmp
        N = len(days)
        day_pass = [1, 7, 30]
        res = min(solve(0,0), solve(0,1), solve(0,2))
        return res

# Main section
for days, costs in [
                      ([1,4,6,7,8,20], [2,7,15]),
                      ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]),
                      ([7,18,20,31,36,90,98,106,108,173,174,178,199,241,247,302,306,307,345,347], [123,590,708]),
                      ([1,6,14,23,27,28,32,34,37,40,45,47,58,62,66,67,73,77,78,80,87,89,95,96,98,111,119,120,121,126,127,131,132,134,137,140,144,150,161,166,177,180,183,188,191,199,200,205,206,211,214,218,219,227,236,238,239,240,241,242,244,246,248,250,254,261,268,269,273,277,286,289,290,291,295,306,309,311,322,328,333,342,348,350,351,353,355,360], [123,590,708]),
                      ([1,2,3,5,8,9,11,12,14,17,18,20,21,22,23,24,27,29,31,33,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,61,62,64,65,66,67,69,71,72,73,75,76,78,82,84,85,86,90,91,92,94,97,101,103,104,105,106,107,108,111,113,115,116,117,118,119,121,122,123,124,125,127,129,132,133,134,136,137,139,141,142,144,145,147,149,150,152,154,155,158,159,160,161,162,165,166,167,169,171,172,173,176,177,180,181,185,186,191,194,195,197,199,200,202,203,205,208,210,211,216,226,227,228,231,235,236,240,243,244,245,246,248,249,252,253,256,257,259,260,261,267,268,269,270,271,273,277,279,280,282,283,286,287,288,289,291,296,297,298,299,300,303,306,310,311,313,314,316,318,325,330,333,334,335,337,338,341,342,344,345,347,349,353,355,356,357,358,360,362], [123,590,708]),
                   ]:
    print(f'days  = {days}')
    print(f'costs = {costs}')
    sol = Solution()
    r = sol.mincostTickets(days, costs)
    print(f'r     = {r}')
    r1 = sol.mincostTickets_1(days, costs)
    print(f'r1    = {r1}')
    print('======================')


