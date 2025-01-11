import math

class Solution:
    def minOperations(self, n: int) -> int:
        powers = [2**i for i in range(round(math.log(10**5) / math.log(2)) + 1)]
        cnt = 0
        while n > 0:
            x = math.floor(math.log(n)/math.log(2))
            y = x + 1
            n = min(abs(n - powers[x]), abs(n - powers[y]))
            cnt += 1
        return cnt

# Main section
for n in [
            39,
            54,
            100000,
            1,
            99999,
            37839,
            883,
            9876,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.minOperations(n)
    print(f'r = {r}')
    print('==============')


