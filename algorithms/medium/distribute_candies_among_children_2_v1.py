class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # After we deduct the candies (i) given to the 1st kid, how do we distribute
        # the remaining candies between 2 kids where max = limit and the total must
        # be the left over amount? Try out a few scenarios with pen and paper. The
        # candy distribution between 2 kids will be as follows:
        # a) the max candy a kid can get is min(limit, leftover)
        # b) if A gets the max amount, then B will get leftover - min(limit, leftover) candies
        # Let v = min(limit, leftover) Then the range of distributions is: [leftover - v, v]
        # This equals: v - (leftover - v) + 1 different ways. That's the main intuition.
        res = 0
        for i in range(0, limit+1):
            candies_left_after_i = n - i
            if candies_left_after_i < 0 or candies_left_after_i > 2 * limit:
                continue
            val = min(limit, candies_left_after_i)
            res += 2 * val - candies_left_after_i + 1
        return res

# Main section
for n, limit in [
                   (5, 2),
                   (3, 3),
                   (1000, 300),
                   (1000000, 990991),
                ]:
    print(f'n, limit = {n}, {limit}')
    sol = Solution()
    r = sol.distributeCandies(n, limit)
    print(f'r = {r}')
    print('=======================')



















