#
# Naive solution throws TLE for last two testcases.
# Memoized solution (countGoodStrings_1) works for them.
#
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def solve(size):
            if size > high:
                return 0
            if size >= low:
                tmp = 1
            else:
                tmp = 0
            tmp += solve(size + zero) + solve(size + one)
            return tmp
        MOD = 10**9 + 7
        res = solve(0)
        return res % MOD
    def countGoodStrings_1(self, low: int, high: int, zero: int, one: int) -> int:
        def solve(size):
            if size > high:
                return 0
            if size in memo:
                return memo[size]
            if size >= low:
                tmp = 1
            else:
                tmp = 0
            tmp += solve(size + zero) + solve(size + one)
            memo[size] = tmp % MOD
            return memo[size]
        memo = dict()
        MOD = 10**9 + 7
        res = solve(0)
        print(memo)
        return res

# Main section
for low, high, zero, one in [
                               (3, 3, 1, 1),
                               (2, 3, 1, 2),
                               (2, 7, 1, 1),
                               (2, 17, 2, 2),
                               #(200, 200, 10, 1),
                               #(500, 500, 1, 1),
                            ]:
    print(f'low, high, zero, one = {low}, {high}, {zero}, {one}')
    sol = Solution()
    #r = sol.countGoodStrings(low, high, zero, one)
    #print(f'r  = {r}')
    r1 = sol.countGoodStrings_1(low, high, zero, one)
    print(f'r1 = {r1}')
    print('================')


