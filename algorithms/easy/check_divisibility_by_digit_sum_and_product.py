from functools import reduce

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def num_iter(n, op):
            res = 0 if op == 'sum' else 1
            while n > 0:
                q, r = divmod(n, 10)
                if op == 'sum':
                    res += r
                elif op == 'prod':
                    res *= r
                n = q
            return res
        digit_sum = num_iter(n, 'sum')
        digit_product = num_iter(n, 'prod')
        return n % (digit_sum + digit_product) == 0
    def checkDivisibility_1(self, n: int) -> bool:
        digit_sum = sum([int(d) for d in str(n)])
        digit_product = reduce(lambda x,y: x*y, [int(d) for d in str(n)])
        return n % (digit_sum + digit_product) == 0

# Main section
for n in [
            99,
            23,
            12345,
            10101,
            1000,
         ]:
    print(f'n  = {n}')
    sol = Solution()
    r = sol.checkDivisibility(n)
    r1 = sol.checkDivisibility_1(n)
    print(f'r  = {r}')
    print(f'r1 = {r}')
    print('============================')
















