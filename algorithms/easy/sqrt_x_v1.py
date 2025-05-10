import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton-Raphson method: x(n+1) = x(n) - ( f(x(n)) / f'(x(n)) )
        # f(n) = n^2 - x and f'(n) = 2*n
        tolerance = 0.000001
        curr_guess = 100
        while True:
            next_guess = curr_guess - ((curr_guess * curr_guess - x) / (2 * curr_guess))
            if abs(next_guess - curr_guess) <= tolerance:
                break
            curr_guess = next_guess
        return int(next_guess)

# Main section
for x in [
            4,
            8,
            0,
            2147483647,
            2147395600,
            398492824,
            101,
            1522756,
         ]:
    print(f'x = {x}')
    sol = Solution()
    r = sol.mySqrt(x)
    print(f'r = {r}')
    assert(int(math.sqrt(x)) == r)
    print('============================')

