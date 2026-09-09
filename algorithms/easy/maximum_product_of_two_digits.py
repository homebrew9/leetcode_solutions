from operator import mul
from functools import reduce

class Solution:
    def maxProduct(self, n: int) -> int:
        return reduce(mul, list(map(int, sorted(str(n))))[-2:])

    def maxProduct_1(self, n: int) -> int:
        return reduce(lambda x,y: x*y, map(int, sorted(str(n))[-2:]))

    def maxProduct_2(self, n: int) -> int:
        x, y = sorted(str(n))[-2:]
        return int(x) * int(y)

    def maxProduct_3(self, n: int) -> int:
        arr = [0 for _ in range(10)]
        while n > 0:
            q, r = divmod(n, 10)
            arr[r] += 1
            n = q
        i = 9
        cnt = 2
        res = 1
        while i >= 0 and cnt > 0:
            if arr[i] != 0:
                if arr[i] > 1 and cnt > 1:
                    res = i * i
                    break
                res *= i
                cnt -= 1
            i -= 1
        return res

    def maxProduct_4(self, n: int) -> int:
        arr = [0 for _ in range(10)]
        while n > 0:
            q, r = divmod(n, 10)
            arr[r] += 1
            n = q
        res = 1
        count = 2
        i = 9
        while count > 0:
            if arr[i] >= 2:
                if count == 2:
                    res *= i * i
                    count -= 2
                elif count == 1:
                    res *= i
                    count -= 1
            elif arr[i] == 1:
                res *= i
                count -= 1
            i -= 1
        return res

# Main section
for n in [
            31,
            22,
            124,
            1000000000,
            292019875,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.maxProduct(n)
    r1 = sol.maxProduct_1(n)
    r2 = sol.maxProduct_2(n)
    r3 = sol.maxProduct_3(n)
    r4 = sol.maxProduct_4(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r3 = {r3}')
    print(f'r4 = {r4}')
    print('===================================')























