#
# StefanPochmann's recursive solution
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

# Main section
for x, n in [
               (2.00000, 10),
               (2.10000, 3),
               (2.10000, 0),
               (2.00000, -2),
               (3, 7),
               (3, 8),
               (3, -7),
               (3, -8),
               (-3, -7),
               (-3, -8),
               (0.00001, 2147483647),
            ]:
    print(f'x, n = {x}, {n}')
    sol = Solution()
    r = sol.myPow(x, n)
    print(f'r = {r}')
    print('=============')

