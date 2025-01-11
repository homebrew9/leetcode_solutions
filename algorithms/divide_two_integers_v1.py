class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Elementary school long division method.
        # https://leetcode.com/problems/divide-two-integers/discuss/218159/Long-Division-Python
        def adjust_value(val):
            max_int = 2**31 - 1
            min_int = -2**31
            if val > max_int:
                val = max_int
            elif val < min_int:
                val = min_int
            return val

        def div(num, den):
            qtt = 0
            while num >= den:
                qtt += 1
                num -= den
            return (qtt, num)

        if dividend == 0:
            return 0
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            ret = adjust_value(sign*dividend)
            return ret

        arr = list()
        dvd = str(dividend)
        dvs = str(divisor)
        chunk = dvd[:len(dvs)]
        left = dvd[len(dvs):]
        while True:
            (qt, rm) = div(int(chunk), divisor)
            #print(f'\t>>> qt, rm = {qt}, {rm}')
            arr.append(qt)
            if left == '':
                break
            chunk = str(rm) + left[:1]
            left = left[1:]
        ret = sign * int(''.join([str(i) for i in arr]))
        ret = adjust_value(ret)
        return ret

# Main section
sol = Solution()
for dividend, divisor in [
                            (-2147483648, -1),
                            (11, 3),
                            (11, -3),
                            (-11, 3),
                            (-11, -3),
                            (0, 3),
                            (5, 1),
                            (-5, 1),
                            (53, -1),
                            (-53, -1),
                            (2147483648, 1),
                            (2147483648, -1),
                            (-2147483648, -1),
                            (-2147483649, 1),
                            (-2147483647, 1),
                            (-2147483648, 2),
                            (2147483647, 2),
                            (1334901, 12),
                            (1134901, 12),
                            (355, 113),
                         ]:
    print(f'dividend, divisor = {dividend}, {divisor}')
    r = sol.divide(dividend, divisor)
    print(f'r = {r}')
    print('=============================')


