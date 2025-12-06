from functools import cache

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        def solve(n):
            if arr[n] != 0:
                return arr[n]
            res = 0
            for i in range(2, n+1, 2):
                inside, outside = i-2, n-i
                res += solve(inside) * solve(outside)
            arr[n] = res
            return arr[n] % MOD
        MOD = 10**9 + 7
        arr = [0] * (numPeople + 1)
        arr[0] = 1
        return solve(numPeople)
    def numberOfWays_1(self, numPeople: int) -> int:
        @cache
        def solve(n):
            if n == 0:
                return 1
            res = 0
            # i is the number of people in the "inside" group + 2 (the handshake pair)
            for i in range(2, n+1, 2):  # i = 2, 4, ..., n
                inside = i - 2
                outside = n - i
                res = (res + solve(inside) * solve(outside)) % MOD
            return res
        MOD = 10**9 + 7
        return solve(numPeople)
    def numberOfWays_2(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (numPeople + 1)
        dp[0] = 1
        for n in range(2, numPeople + 1, 2):
            for i in range(1, n, 2):
                left = i - 1
                right = n - i - 1
                dp[n] = (dp[n] + dp[left] * dp[right]) % MOD
        return dp[numPeople]

# Main section
for numPeople in [
                    4,
                    6,
                    94,
                    356,
                    1000,
                 ]:
    print(f'numPeople = {numPeople}')
    sol = Solution()
    r = sol.numberOfWays(numPeople)
    r1 = sol.numberOfWays_1(numPeople)
    r2 = sol.numberOfWays_2(numPeople)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    assert(r == r1 == r2)
    print('===========================')






















