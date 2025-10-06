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

    def numWaterBottles_1(self, numBottles: int, numExchange: int) -> int:
        filled, empty = numBottles, 0
        res = 0
        while True:
            # Drink the filled bottles
            res += filled
            empty += filled
            # Now exchange the empty bottles if possible
            if empty < numExchange:
                break
            filled, empty = divmod(empty, numExchange)
        return res

# Main section
for numBottles, numExchange in [
                                  (9, 3),
                                  (15, 4),
                               ]:
    print(f'numBottles, numExchange = {numBottles}, {numExchange}')
    sol = Solution()
    r = sol.numWaterBottles(numBottles, numExchange)
    r1 = sol.numWaterBottles_1(numBottles, numExchange)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=====================')





