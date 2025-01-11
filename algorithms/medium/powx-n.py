class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = False
        if n < 1:
            neg = True
            n = abs(n)
        hsh = dict()
        res = x
        exp = 1
        hsh[exp] = res
        while exp * 2 <= n:
            res *= res
            exp *= 2
            hsh[exp] = res
        #print(hsh, n-exp)
        for k in sorted(hsh.keys(), reverse=True):
            if exp + k <= n:
                res *= hsh[k]
                exp += k
        if neg:
            res = 1 / res
        return res

# Main section
for x, n in [
               (2.00000, 10),
               (2.10000, 3),
               (2.00000, -2),
               (3, 7),
               (3, 8),
               (3, -7),
               (3, -8),
               (-3, -7),
               (-3, -8),
            ]:
    print(f'x, n = {x}, {n}')
    sol = Solution()
    r = sol.myPow(x, n)
    print(f'r = {r}')
    print('=============')

