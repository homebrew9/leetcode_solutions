class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i % m != 0:
                res += i
            else:
                res -= i
        return res
    def differenceOfSums_1(self, n: int, m: int) -> int:
        return sum([-i if i % m == 0 else i for i in range(1, n+1)])
    def differenceOfSums_2(self, n: int, m: int) -> int:
        ''' n = 10, m = 3
            Total Sum = n * (n+1) / 2
            Sum of multiples of 3 = AP = n/2 * (a1 + aN)
            Answer = Total_Sum - 2 * Sum_of_multiples_of_m
        '''
        total_sum = n * (n + 1) // 2
        first, last = m, m * (n // m)
        size = n // m
        sum_of_multiples = (size * (first + last)) // 2
        return total_sum - 2 * sum_of_multiples

# Main section
for n, m in [
               (10, 3),
               (5, 6),
               (5, 1),
               (997, 13),
               (1000, 1),
            ]:
    print(f'n, m = {n}, {m}')
    sol = Solution()
    r = sol.differenceOfSums(n, m)
    r1 = sol.differenceOfSums_1(n, m)
    r2 = sol.differenceOfSums_2(n, m)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print(f'r2   = {r2}')
    print('============================')







