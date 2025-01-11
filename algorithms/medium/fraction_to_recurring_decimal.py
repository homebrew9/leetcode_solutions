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
            print(f'\tres, p, q, hsh = {res}, {p}, {q}, {hsh}')
            if q in hsh:
                return sign + res[:hsh[q]] + '(' + res[hsh[q]:] + ')'
            hsh[q] = len(res)
            q *= 10
            p, q = divmod(q, denominator)
            res += str(p)
        return sign+res

# Main section
for numerator, denominator in [
                                 #(1, 7),
                                 #(1, 2),
                                 #(2, 1),
                                 #(4, 333),
                                 #(1, 88),
                                 #(1, 888),
                                 #(232837287, 5669),
                                 #(17, 8),
                                 #(1, 21),
                                 #(1, 17),
                                 #(-50, 8),
                                 (7, -12),
                              ]:
    print(f'numerator, denominator = {numerator}, {denominator}')
    sol = Solution()
    r = sol.fractionToDecimal(numerator, denominator)
    print(f'r = {r}')
    print('==============')


