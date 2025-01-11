class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton's method to find square root:
        # Given an estimate x0, a better estimate x1 is: x1 = x0 - f(x0)/f'(x0)
        # Here: f(x) = x^2 - num and hence f'(x) = 2x
        # Unfortunately - this method does not work correctly for num = 16 !!
        # The value of the root (x) is always a floating-point close to 4, but not 4
        tolerance = 0.1
        x = num
        print(f'x, x^2, num, (x^2-num), abs(x^2-num) = {x}, {x*x}, {num}, {x*x-num}, {abs(x*x-num)}')
        while abs(x*x - num) > tolerance:
            x = x - (x*x - num)/2/x
            print(f'\tx, x^2, num, (x^2-num), abs(x^2-num) = {x}, {x*x}, {num}, {x*x-num}, {abs(x*x-num)}')
        print(f'x = {x}')
        return x == int(x)

# Main section
sol = Solution()
for num in [
              16,
              2147395600,
              1,
              1867104100,
              145,
              362,
              1295064168,
              680635927,
           ]:
    print(f'num = {num}')
    r = sol.isPerfectSquare(num)
    print(f'r = {r}')
    print('======================')


