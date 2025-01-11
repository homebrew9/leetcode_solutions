#
# Interesting problem. Takes a while to understand that divmod() can be used here.
#
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles
        while numBottles >= numExchange:
            p, q = divmod(numBottles, numExchange)
            cnt += p
            numBottles = p + q
        return cnt

# Main section
for numBottles, numExchange in [
                                  (9, 3),
                                  (15, 4),
                               ]:
    print(f'numBottles, numExchange = {numBottles}, {numExchange}')
    sol = Solution()
    r = sol.numWaterBottles(numBottles, numExchange)
    print(f'r = {r}')
    print('=====================')

