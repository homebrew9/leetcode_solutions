class Solution:
    def largestInteger(self, num: int) -> int:
        evens, odds = list(), list()
        orig = num
        while num > 0:
            p, q = divmod(num, 10)
            if q % 2 == 1:
                odds.append(q)
            else:
                evens.append(q)
            num = p
        evens.sort()
        odds.sort()

        #print(f'\tevens, odds = {evens}, {odds}')
        res = 0
        i, j = 0, 0
        pv = 1
        while orig > 0:
            p, q = divmod(orig, 10)
            if q % 2 == 1:
                res = odds[i] * pv + res
                i += 1
            else:
                res = evens[j] * pv + res
                j += 1
            orig = p
            pv *= 10
        return res

# Main section
for num in [
              1234,
              65875,
              123456789,
              987654321,
              100,
              1001,
              1010,
              90705030,
              30507090,
              247,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.largestInteger(num)
    print(f'r = {r}')
    print('================')


