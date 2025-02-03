class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # The maximum distance would be achieved if we keep going on the diagonals: NE, NW, SE, SW
        # Go through each diagonal one-by-one and try to greedily increase the distance
        # as much as possible.
        diagonals = [('N','E'), ('N','W'), ('S','E'), ('S','W')]
        res = 0
        for diag in diagonals:
            curr = 0
            iter_k = k
            for ch in s:
                if ch in diag:
                    curr += 1
                elif iter_k > 0:
                    curr += 1
                    iter_k -= 1
                else:
                    curr -= 1
                res = max(res, curr)
        return res

# Main section
for s, k in [
               ('NWSE', 1),
               ('NSWWEW', 3),
               ('NSES', 1),
               ('EWWE', 1),
               ('WEEW', 3),
               ('WEWE', 1),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.maxDistance(s, k)
    print(f'r = {r}')
    print('=======================')

