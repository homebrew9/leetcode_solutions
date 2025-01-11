import math
class Solution:
    # Unfortunately, I could not make this work!!
    # Still need to spend more time to understand this one!
    def adjust_value(self, val):
        max_int = 2**31 - 1
        min_int = -2**31
        if val > max_int:
            val = max_int
        elif val < min_int:
            val = min_int
        return val

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 1:
            ret = self.adjust_value(dividend)
            return ret
        if divisor == -1:
            ret = self.adjust_value(-dividend)
            return ret
        final_sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            final_sign = -1
        if dividend < 0:
            num = -dividend
        else:
            num = dividend
        if divisor < 0:
            den = -divisor
        else:
            den = divisor
        # ======================================================
        # Using log10 returns incorrect result for (-2147483648, 2). It returns
        # -1073741823 because 10**(math.log10(2147483648) - math.log10(2)) = 1073741823.9999999
        # whereas 2**(math.log(2147483648,2) - math.log(2,2)) = 1073741824.0000026
        # Looks like a corner case.
        # ======================================================
        ret = final_sign * int(round(2**(math.log(num,2) - math.log(den,2))))
        ret = self.adjust_value(ret)
        return ret

# Main section
sol = Solution()
for dividend, divisor in [
                            #(-2147483648, -1),
                            #(11, 3),
                            #(11, -3),
                            #(-11, 3),
                            #(-11, -3),
                            #(0, 3),
                            #(5, 1),
                            #(-5, 1),
                            #(53, -1),
                            #(-53, -1),
                            #(2147483648, 1),
                            #(2147483648, -1),
                            #(-2147483648, -1),
                            #(-2147483649, 1),
                            #(-2147483647, 1),
                            #(-2147483648, 2),
                            (2147483647, 2),
                         ]:
    print(f'dividend, divisor = {dividend}, {divisor}')
    r = sol.divide(dividend, divisor)
    print(f'r = {r}')
    print('=============================')

