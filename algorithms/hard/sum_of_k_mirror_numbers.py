class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def palindromic_pattern(n):
            # Notice the pattern to generate palindromic numbers of length n.
            # If n == 6, then: 100|001, 101|101, 102|201, ... 998|899, 999|999 i.e. (999 - 100 + 1) numbers
            # If n == 7, then: 100|0|001, 100|1|001, ... 100|9|001, 101|0|001, ... 999|9|999 i.e. (999 - 100 + 1) * 10 numbers
            if n == 1:
                return list(range(1,10))
            res = list()
            k = n // 2
            lim = 10**k
            if n % 2 == 1:
                for i in range(lim//10, lim):
                    for j in range(0, 10):
                        res.append(int(str(i) + str(j) + str(i)[::-1]))
            else:
                for i in range(lim//10, lim):
                    res.append(int(str(i) + str(i)[::-1]))
            return res
        def convert2basen(n, b):
            # Convert a base 10 integer n to base b. 2 <= b <= 9.
            # Return the final integer.
            res = ''
            while n > 0:
                q, r = divmod(n, b)
                res = str(r) + res
                n = q
            return res
        res = 0
        for i in range(1, 100):
            for num in palindromic_pattern(i):
                val = convert2basen(num, k)
                if val == val[::-1]:
                    res += num
                    n -= 1
                    if n == 0:
                        return res

# Main section
for k, n in [
               (2, 5),
               (3, 7),
               (7, 17),
               (9, 30),
            ]:
    print(f'k, n = {k}, {n}')
    sol = Solution()
    r = sol.kMirror(k, n)
    print(f'r = {r}')
    print('=======================')























