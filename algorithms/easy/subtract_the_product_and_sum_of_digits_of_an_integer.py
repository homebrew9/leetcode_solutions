class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digits, prod_digits = 0, 1
        while n > 0:
            q, r = divmod(n, 10)
            sum_digits += r
            prod_digits *= r
            n = q
        return (prod_digits - sum_digits)

# Main section
for n in [
            234,
            4421,
            1,
            5,
            9,
            1000,
            8986,
            98765,
            100000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.subtractProductAndSum(n)
    print(f'r = {r}')
    print('==============')

