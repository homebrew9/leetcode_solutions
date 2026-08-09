class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        arr = [0 for _ in range(n)]
        for i in range(n):
            tmp = min(9, s)
            arr[i] = tmp
            s -= tmp
        if s > 0:
            return -1
        res = 0
        for i in range(n):
            res = 10 * res + arr[i]
        return res
    def largestInteger_1(self, n: int, s: int) -> int:
        res = 0
        while n > 0 or s > 0:
            tmp = 0
            if s > 0:
                tmp = min(9, s)
                s -= tmp
            res = 10 * res + tmp
            n -= 1
            if n < 0:
                return -1
        return res
    def largestInteger_2(self, n: int, s: int) -> int:
        res = 0
        digits = 0
        while s > 0:
            tmp = min(9, s)
            s -= tmp
            res = 10 * res + tmp
            digits += 1
            if digits > n:
                return -1
        return res * 10**(max(n - digits, 0))
    def largestInteger_3(self, n: int, s: int) -> int:
        res = 0
        digits = 0
        while s > 0:
            tmp = min(9, s)
            s -= tmp
            res = 10 * res + tmp
            digits += 1
        return -1 if digits > n else res * 10**(max(n - digits, 0))

# Main section
for n, s in [
               (2, 9),
               (2, 19),
               (5, 0),
               (4, 22),
               (5, 22),
               (5, 45),
               (5, 10),
               (1, 100),
            ]:
    print(f'n, s = {n}, {s}')
    sol = Solution()
    r = sol.largestInteger(n, s)
    r1 = sol.largestInteger_1(n, s)
    r2 = sol.largestInteger_2(n, s)
    r3 = sol.largestInteger_3(n, s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r3 = {r3}')
    print('===================================')









