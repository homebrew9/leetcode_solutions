class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        filled, empty = numBottles, 0
        res = 0
        while True:
            # Drink the filled bottles
            res += filled
            empty += filled
            # Now exchange the empty bottles if possible
            if empty < numExchange:
                break
            #filled, empty = divmod(empty, numExchange)
            filled, empty = 1, empty - numExchange
            numExchange += 1
        return res

# Main section
for numBottles, numExchange in [
                                  (13, 6),
                                  (10, 3),
                               ]:
    print(f'numBottles, numExchange = {numBottles}, {numExchange}')
    sol = Solution()
    r = sol.maxBottlesDrunk(numBottles, numExchange)
    print(f'r = {r}')
    print('=====================')

