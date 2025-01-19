#
# Using eval - this is slower than the stack solution. Also, I am unable to
# make it work in my environment. It works in the OJ. I encounter RecursionError
# for a few testcases despite setting the recursion limit to a very high value.
#
import sys

class Solution:
    def clumsy(self, n: int) -> int:
        operations = ['*', '//', '+', '-']
        num = n
        i = 0
        s = str(num)
        while num > 1:
            num -= 1
            s += operations[i] + str(num)
            i = (i + 1) % len(operations)
        return eval(s)

# Main section
sys.setrecursionlimit(10**9)
for n in [
            4,
            10,
            #10000,
            3437,
            3599,
            103,
            101,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            #7328,
            #9999,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.clumsy(n)
    print(f'r = {r}')
    print('================')

            

