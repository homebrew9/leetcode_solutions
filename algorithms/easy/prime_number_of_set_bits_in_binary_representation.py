class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Upper limit 10^6 has 20 bits
        primes = {2,3,5,7,11,13,17,19}
        res = 0
        for n in range(left, right+1):
            if bin(n)[2:].count('1') in primes:
                res += 1
        return res

# Main section
for left, right in [
                      (6, 10),
                      (10, 15),
                   ]:
    print(f'left, right = {left}, {right}')
    sol = Solution()
    r = sol.countPrimeSetBits(left, right)
    print(f'r = {r}')
    print('=================================================')
 























