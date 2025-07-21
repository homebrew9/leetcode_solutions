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

# Main section
for n in [
            99,
            23,
            12345,
            10101,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.checkDivisibility(n)
    print(f'r = {r}')
    print('============================')




















