#
# Important note: I am unable to fix the max recursion error in solutions 1 and 2 here,
# but the solution passes the LC OJ. The error is "RecursionError: maximum recursion depth exceeded"
#
from typing import List
from functools import cache
from collections import defaultdict

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def solve(i, j, t):
            if i == j:
                if t >= mid:
                    self.res = True
                return
            solve(i + 1, j, t + piles[i])
            solve(i, j - 1, t + piles[j])
        N = len(piles)
        mid = sum(piles)//2 + 1
        self.res = False
        solve(0, N-1, 0)
        return self.res

    def stoneGame_1(self, piles: List[int]) -> bool:
        @cache
        def solve(i, j):
            if i == j:
                return 0
            res = max(piles[i] + solve(i + 1, j), piles[j] + solve(i, j - 1))
            return res
        N = len(piles)
        mid = sum(piles)//2 + 1
        ans = solve(0, N-1)
        return ans >= mid

    def stoneGame_2(self, piles: List[int]) -> bool:
        def solve(i, j):
            if i == j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = max(piles[i] + solve(i + 1, j), piles[j] + solve(i, j - 1))
            memo[(i, j)] = res
            return res
        N = len(piles)
        mid = sum(piles)//2 + 1
        memo = defaultdict(int)
        ans = solve(0, N-1)
        return ans >= mid

# Main section
import sys
sys.setrecursionlimit(1000_000_000)
for piles in [
                [5,3,4,5],
                [3,7,2,3],
                [37,54,49,24,9,94,63,54,7,25,25,51,92,50,7,97,65,56,90,43,4,45,87,89,47,50,80,55,23,52,27,95,82,41,43,25,49,74,70,80,68,49,98,99,51,65,51,24,70,90,85,47,62,87,40,5,33,37,5,57,90,31,29,69,91,40,36,35,71,76,31,38,38,60,2,40,24,44,54,7,29,26,21,83,28,95,93,93,100,90,88,42,15,93,89,47,83,24,34,93],
                [107,153,340,21,328,153,71,297,115,486,268,47,369,297,356,427,305,25,87,85,280,372,27,269,190,28,13,466,420,329,408,75,457,255,454,296,273,83,357,40,57,25,87,218,393,428,493,48,384,173,384,349,448,334,114,98,318,383,442,13,192,496,45,267,62,178,151,360,325,131,16,383,256,314,464,416,114,132,382,338,427,294,390,208,191,390,360,204,52,343,237,419,295,67,218,495,488,234,499,139,293,211,148,125,288,439,450,259,175,445,342,166,191,263,74,130,270,172,272,39,17,356,380,412,156,112,348,216,350,90,212,46,209,496,143,408,65,471,54,382,417,464,207,273,270,328,255,240,144,187,169,94,102,267,136,375,291,8,385,139,279,59,328,304,36,223,382,172,103,352,58,403,297,302,316,140,468,441,215,91,299,185,12,404,241,292,424,26,115,44,284,287,177,422,163,304,342,49,362,43,31,52,206,172,155,327,325,112,440,431,156,17,5,378,177,57,39,203,382,470,473,271,475,354,304,208,450,15,469,215,3,181,124,130,265,429,316,401,357,175,344,140,244,250,290,252,134,446,173,434,235,255,177,108,368,15,61,272,348,162,241,145,345,449,191,213,438,93,75,179,60,188,253,287,344,89,326,392,188,341,341,262,327,404,338,268,424,338,40,238,203,469,338,242,290,433,493,65,15,4,54,38,31,175,111,97,31,219,48,68,213,57,416,164,17,477,54,219,335,183,434,201,241,16,162,206,167,276,38,72,192,265,437,402,255,365,322,477,417,292,318,441,16,214,411,224,54,165,347,456,258,104,26,170,405,60,119,9,442,235,105,408,363,3,346,383,164,471,421,146,487,408,195,385,395,225,457,353,307,278,63,458,498,236,453,171,428,341,71,151,280,206,189,416,113,161,220,360,28,9,496,174,470,474,411,382,84,312,247,402,30,75,245,354,400,292,250,381,5,231,236,92,299,268,461,265,449,337,39,239,450,91,20,58,64,202,36,309,21,242,369,31,322,169,352,416,382,430,441,84,402,264,482,281,124,48,59,17,175,318,184,5,117,241,278,388,209,292,254,260,405,415,485,127,420,144,122,101,58,362,83,366,272,495,392,180,454,112,210,44,240,455,223,151,283,490,474,424,476,202],
                [1,9,8,1],
            ]:
    print(f'piles = {piles}')
    sol = Solution()
    #r = sol.stoneGame(piles)
    #print(f'r = {r}')
    #r1 = sol.stoneGame_1(piles)
    #print(f'r1 = {r1}')
    r2 = sol.stoneGame_2(piles)
    print(f'r2 = {r2}')
    print('===================')


