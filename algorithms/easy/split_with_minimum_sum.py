#
# TLE for last test case!
#
from itertools import permutations

class Solution:
    def splitNum(self, num: int) -> int:
        def fetchOther(arr, tpl):
            #print(f'\t\tarr, tpl = {arr}, {tpl}')
            for t in tpl:
                if t in arr:
                    arr.remove(t)
            #print(f'\t\tret = {arr}')
            #print(f'\t\t====')
            return ''.join(arr)
        s = str(num)
        arr = list(s)
        N = len(s)
        min_sum = float('inf')
        for k in range(1, N):
            for tpl in list(permutations(s, k)):
                other = fetchOther(list(s), tpl)
                #print(f'\ttpl, other = {tpl}, {other}')
                M = len(other)
                for tpl1 in list(permutations(other, M)):
                    #print(f'\ttpl, tpl1 = {tpl}, {tpl1}')
                    curr_sum = int(''.join(tpl)) + int(''.join(tpl1))
                    if curr_sum == 1:
                        return curr_sum
                    min_sum = min(min_sum, curr_sum)
        return min_sum

# Main section
for num in [
              #4325,
              #687,
              1234567,
              #1000000000,
              #999999999,
              857172936,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.splitNum(num)
    print(f'r = {r}')
    print('=================')

