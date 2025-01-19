import math
class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        def solve(arr, N):
            if len(arr) == n:
                self.res += 1
                return
            for num in num_set:
                if num not in arr and math.gcd(num, N) == 1:
                    solve(arr + [num], N+1)
        num_arr = [i for i in range(1, n+1)]
        num_set = set(num_arr)
        self.res = 0
        solve([], 1)
        return self.res

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.selfDivisiblePermutationCount(n)
    print(f'r = {r}')
    print('==============')


