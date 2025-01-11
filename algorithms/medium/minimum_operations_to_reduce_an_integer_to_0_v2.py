import math

class Solution:
    def minOperations(self, n: int) -> int:
        def minOps(n):
            if n == 0:
                return
            x = math.floor(math.log(n)/math.log(2))
            y = x + 1
            n = min(abs(n - self.powers[x]), abs(n - self.powers[y]))
            self.cnt += 1
            minOps(n)
        self.powers = [2**i for i in range(round(math.log(10**5) / math.log(2)) + 1)]
        self.cnt = 0
        minOps(n)
        return self.cnt

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



