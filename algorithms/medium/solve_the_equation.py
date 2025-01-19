from typing import List
import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        def get_coeff_const(arr):
            coeff, const = 0, 0
            for item in arr:
                try:
                    const += int(item)
                except:
                    pfx = item.replace('x', '')
                    if pfx == '' or pfx == '+':
                        coeff += 1
                    elif pfx == '-':
                        coeff -= 1
                    else:
                        coeff += int(pfx)
            return (coeff, const)
        left_side, right_side = equation.split('=')
        left_arr = re.findall(r'([+-]*x|[+-]*\d+x|[+-]*\d+)', left_side)
        right_arr = re.findall(r'([+-]*x|[+-]*\d+x|[+-]*\d+)', right_side)
        left_coeff, left_const = get_coeff_const(left_arr)
        right_coeff, right_const = get_coeff_const(right_arr)
        coeff_x = left_coeff - right_coeff
        constant = left_const - right_const
        #print(coeff_x, constant)
        res = ''
        if coeff_x == 0:
            if constant == 0:
                res = 'Infinite solutions'
            else:
                res = 'No solution'
        else:
            val = -constant // coeff_x
            res = f'x={val}'
        return res

# Main section
for equation in [
                   'x+5-3+x=6+x-2',
                   'x=x',
                   '2x=x',
                   '5=5',
                   '5=6',
                   '-3x+657-113+7-9-119+x-4+7x+24=49x-76+124-13x+x-2x-x+67-36-x',
                   '-10+12-34-90+45+87-87-21=49-76+124-13+1-2-1+67-36-1',
                   '-10+12-34-90+45+87-87-21=49-76+124-13+1-2-1+67-36-1-x',
                ]:
    print(f'equation = [{equation}]')
    sol = Solution()
    r = sol.solveEquation(equation)
    print(f'r        = [{r}]')
    print('==================')


