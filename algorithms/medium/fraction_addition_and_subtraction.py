#import math
class Solution:
    #def fractionAddition(self, expression: str) -> str:
    #    def fetch_num(i):
    #        neg = False
    #        if expression[i] == '-':
    #            neg = True
    #            i += 1
    #        res = ''
    #        while i < N and expression[i] in '0123456789':
    #            res += expression[i]
    #            i += 1
    #        res = int(res)
    #        if neg:
    #            res = -res
    #        return (res, i)
    #    def fetch_fraction(i):
    #        nmr, i = fetch_num(i)
    #        if expression[i] == '/':
    #            i += 1
    #        dnr, i = fetch_num(i)
    #        return ([nmr, dnr], i)
    #    def evaluate_expression(frac1, frac2, op):
    #        n1, d1 = frac1
    #        n2, d2 = frac2
    #        if op == '+':
    #            n = (n1 * d2) + (n2 * d1)
    #        elif op == '-':
    #            n = (n1 * d2) - (n2 * d1)
    #        d = d1 * d2
    #        gcd = math.gcd(n, d)
    #        n = n // gcd
    #        d = d // gcd
    #        return (n, d)

    def fractionAddition(self, expression: str) -> str:
        def _gcd(m, n):
            if n == 0:
                return m
            return _gcd(n, m % n)
        def fetch_num(i):
            neg = False
            if expression[i] == '-':
                neg = True
                i += 1
            res = ''
            while i < N and expression[i] in '0123456789':
                res += expression[i]
                i += 1
            res = int(res)
            if neg:
                res = -res
            return (res, i)
        def fetch_fraction(i):
            nmr, i = fetch_num(i)
            if expression[i] == '/':
                i += 1
            dnr, i = fetch_num(i)
            return ([nmr, dnr], i)
        def evaluate_expression(frac1, frac2, op):
            n1, d1 = frac1
            n2, d2 = frac2
            if op == '+':
                n = (n1 * d2) + (n2 * d1)
            elif op == '-':
                n = (n1 * d2) - (n2 * d1)
            d = d1 * d2
            gcd = _gcd(n, d)
            n = n // gcd
            d = d // gcd
            return (n, d)

        N = len(expression)
        frac1, i = fetch_fraction(0)
        while i < N:
            op = expression[i]
            i += 1
            frac2, i = fetch_fraction(i)
            frac1 = evaluate_expression(frac1, frac2, op)
        return f'{frac1[0]}/{frac1[1]}'

# Main section
for expression in [
                     '-1/2+1/2',
                     '-1/2+1/2+1/3',
                     '1/3-1/2',
                     '113/355+113/355-113/355',
                     '16/64-36/75+79/23-19/91+87/56',
                  ]:
    print(f'expression = {expression}')
    sol = Solution()
    r = sol.fractionAddition(expression)
    print(f'r = {r}')
    print('================')

