class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        sign = ''
        if num < 0:
            sign = '-'
            num = -num
        while num > 0:
            res = str(num % 7) + res
            num //= 7
        return sign + res

# Main section
for num in [
              100,
              -7,
              54321,
              0,
              -1,
              -2,
              -3,
              -6,
              -8,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10000000,
              -10000000,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.convertToBase7(num)
    print(f'r = {r}')
    print('===========================')

