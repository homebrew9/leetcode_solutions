#
# Recursive solution - fails for the case where n = 2**31-1
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powRecur(x, n, ans):
            if n == 0:
                return ans
            return powRecur(x, n-1, ans*x)

        if n < 0:
            return 1 / powRecur(x, abs(n), 1)
        return powRecur(x, n, 1)

# Main section
for x, n in [
               #(2.00000, 10),
               #(2.10000, 3),
               #(2.10000, 0),
               #(2.00000, -2),
               #(3, 7),
               #(3, 8),
               #(3, -7),
               #(3, -8),
               #(-3, -7),
               #(-3, -8),
               (0.00001, 2147483647),
            ]:
    print(f'x, n = {x}, {n}')
    sol = Solution()
    r = sol.myPow(x, n)
    print(f'r = {r}')
    print('=============')


