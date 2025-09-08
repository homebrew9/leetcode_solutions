from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(n):
            while n > 0:
                q, r = divmod(n, 10)
                if r == 0:
                    return True
                n = q
            return False
        p = n // 2
        q = n - p
        while has_zero(p) or has_zero(q):
            p -= 1
            q += 1
        return [p, q]
    def getNoZeroIntegers_1(self, n: int) -> List[int]:
        arr = list()
        for i in range(1, n):
            if str(i).count('0') == 0 and str(n-i).count('0') == 0:
                arr += [i, (n-i)]
                break
        return arr
    def getNoZeroIntegers_2(self, n: int) -> List[int]:
        def isNoZero(n):
            while n > 0:
                p, q = divmod(n, 10)
                if q == 0:
                    return False
                n = p
            return True
                
        arr = list()
        for i in range(1, n):
            if isNoZero(i) and isNoZero(n-i):
                arr += [i, (n-i)]
                break
        return arr

# Main section
for n in [
            2,
            11,
            60,
            91,
            7091,
            8080,
            9111,
            1001,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.getNoZeroIntegers(n)
    r1 = sol.getNoZeroIntegers_1(n)
    r2 = sol.getNoZeroIntegers_2(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('=================')























