from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_of_digits(n):
            res = 0
            while n > 0:
                q, r = divmod(n, 10)
                res += r
                n = q
            return res
        hsh = defaultdict(int)
        for i in range(1, n+1):
            sd = sum_of_digits(i)
            hsh[sd] += 1
        max_val = max(hsh.values())
        return sum([v == max_val for v in hsh.values()])

# Main section
for n in [
            13,
            2,
            10000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countLargestGroup(n)
    print(f'r = {r}')
    print('========================')

