from functools import cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def solve(i, j):
            if expression[i:j+1].isdigit():
                return [int(expression[i:j+1])]
            arr = list()
            for k in range(i, j+1):
                if not expression[k].isdigit():
                    op = expression[k]
                    left_arr = solve(i, k-1)
                    right_arr = solve(k+1, j)
                    for lv in left_arr:
                        for rv in right_arr:
                            if op == '+':
                                arr.append(lv + rv)
                            elif op == '-':
                                arr.append(lv - rv)
                            elif op == '*':
                                arr.append(lv * rv)
            return arr
        N = len(expression)
        i, j = 0, N - 1
        res = solve(i, j)
        return res

# Main section
for expression in [
                     '2-1-1',
                     '2*3-4*5',
                     '2*7+3',
                     '2*3-4+5+6*7-8*9+1',
                     '1+2-3*4+5-6*7+8-9*10',
                     '17+37*53-79+83*91-97',
                     '98',
                     '98-98',
                  ]:
    print(f'expression = {expression}')
    sol = Solution()
    r = sol.diffWaysToCompute(expression)
    print(f'r = {r}')
    print(f'len(r) = {len(r)}')
    print('===================')


