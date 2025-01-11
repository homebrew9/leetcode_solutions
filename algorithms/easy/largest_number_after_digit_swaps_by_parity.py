class Solution:
    def largestInteger(self, num: int) -> int:
        evens, odds = '', ''
        for ch in str(num):
            if int(ch) % 2 == 1:
                odds += ch
            else:
                evens += ch

        evens = ''.join(sorted(evens, reverse=True))
        odds = ''.join(sorted(odds, reverse=True))

        res = ''
        i, j = 0, 0
        for ch in str(num):
            if int(ch) % 2 == 1:
                res += odds[i]
                i += 1
            else:
                res += evens[j]
                j += 1

        return int(res)

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

