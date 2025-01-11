#
# Commented code throws TLE for large values of n and limit.
#

#class Solution:
#    def distributeCandies(self, n: int, limit: int) -> int:
#        @cache
#        def check(pos, arr):
#            if pos >= 3:
#                if sum(arr) == n:
#                    self.dist.add(arr)
#                return
#            for i in range(limit+1):
#                if sum(arr[:pos]) <= n:
#                    lst = list(arr)
#                    lst[pos] = i
#                    check(pos+1, tuple(lst))
#        self.dist = set()
#        arr = (0,0,0)
#        check(0, arr)
#        return len(self.dist)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                if n - i - j >= 0 and n - i - j <= limit:
                    res += 1
        return res

for n, limit in [
                   (5, 2),
                   (3, 3),
                   (1000, 300),
                ]:
    print(f'n, limit = {n}, {limit}')
    sol = Solution()
    r = sol.distributeCandies(n, limit)
    print(f'r = {r}')
    print('=======================')

