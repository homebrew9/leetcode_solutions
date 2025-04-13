class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        odd_cardinality = 4   # Primes 2,3,5,7 at odd indexes
        even_cardinality = 5  # Evens 0,2,4,6,8 at even indexes
        odd_inds = n // 2
        if n % 2 == 0:
            even_inds = n // 2
        else:
            even_inds = n // 2 + 1
        #return ((odd_cardinality**odd_inds) * (even_cardinality**even_inds)) % MOD
        # Fast exponentiation using bit manipulation is required here
        ans1 = 1
        while odd_inds > 0:
            if odd_inds & 1 == 1:
                ans1 = (ans1 * odd_cardinality) % MOD
            odd_cardinality = (odd_cardinality * odd_cardinality) % MOD
            odd_inds = odd_inds >> 1
        ans2 = 1
        while even_inds > 0:
            if even_inds & 1 == 1:
                ans2 = (ans2 * even_cardinality) % MOD
            even_cardinality = (even_cardinality * even_cardinality) % MOD
            even_inds = even_inds >> 1
        return (ans1 * ans2) % MOD

# Main section
for n in [
            1,
            4,
            50,
            1000,
            1000000,
            1000000000000000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countGoodNumbers(n)
    print(f'r = {r}')
    print('========================')

