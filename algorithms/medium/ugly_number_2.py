#
# Very smart solution! This is the official LC solution.
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_set = set()
        ugly_set.add(1)
        for _ in range(n):
            curr = min(ugly_set)
            ugly_set.remove(curr)
            ugly_set.add(curr * 2)
            ugly_set.add(curr * 3)
            ugly_set.add(curr * 5)
        return curr

# Main section
hsh = {
         1: 1,
         10: 12,
         59: 375,
         100: 1536,
         250: 38880,
         500: 937500,
         1000: 51200000,
         1500: 859963392,
         1600: 1399680000,
         1690: 2123366400,
      }

for n in [
            1,
            10,
            59,
            100,
            250,
            500,
            1000,
            1500,
            1600,
            1690,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.nthUglyNumber(n)
    print(f'r = {r}')
    assert(r == hsh[n])
    print('=============')


