class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        sign = ''
        if numerator * denominator < 0:
            sign = '-'
        numerator, denominator = abs(numerator), abs(denominator)
        hsh = dict()
        p, q = divmod(numerator, denominator)
        res = str(p) + '.'
        while q != 0:
            #print(f'\tres, p, q, hsh = {res}, {p}, {q}, {hsh}')
            if q in hsh:
                return sign + res[:hsh[q]] + '(' + res[hsh[q]:] + ')'
            hsh[q] = len(res)
            q *= 10
            p, q = divmod(q, denominator)
            res += str(p)
        return sign+res

    def fractionToDecimal_1(self, numerator: int, denominator: int) -> str:
        # Perform long division until the remainder repeats. If it does, we have a recurring decimal.
        # Handle trivial cases, sign etc.
        if numerator == 0:
            return '0'
        if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator > 0):
            pos = True
        else:
            pos = False
        numerator, denominator = abs(numerator), abs(denominator)
        if numerator % denominator == 0:
            val = str(int(numerator / denominator))
            if not pos:
                val = f'-{val}'
            return val
        int_part, r = divmod(numerator, denominator)
        idx = 0
        hsh = {r: idx}
        idx += 1
        res = ''
        is_recurring = True
        for _ in range(10000):
            q, r = divmod(r * 10, denominator)
            res += str(q)
            if r == 0:
                is_recurring = False
                break
            if r in hsh:
                break
            hsh[r] = idx
            idx += 1
        if is_recurring:
            i = hsh[r]
            result = f'{int_part}.{res[:i]}({res[i:]})'
        else:
            result = f'{int_part}.{res}'
        if not pos:
            result = f'-{result}'
        return result

# Main section
for numerator, denominator in [
                                 (1, 7),
                                 (1, 2),
                                 (2, 1),
                                 (4, 333),
                                 (1, 88),
                                 (1, 888),
                                 (232837287, 5669),
                                 (17, 8),
                                 (1, 21),
                                 (1, 17),
                                 (-50, 8),
                                 (7, -12),
                              ]:
    print(f'numerator, denominator = {numerator}, {denominator}')
    sol = Solution()
    r = sol.fractionToDecimal(numerator, denominator)
    r1 = sol.fractionToDecimal_1(numerator, denominator)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('==============')









