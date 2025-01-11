class Solution:
    def findComplement(self, num: int) -> int:
        l = len(bin(num).replace('0b',''))
        return int(bin(2**31 - 1 - num).replace('0b','')[-l:], 2)

# Main section
for num in [
              5,
              1,
              2564738,
              2147483647,
              233,
              4567,
              12345,
              473828,
              8475839,
              10009289,
              589076540,
           ]:
    sol = Solution()
    print(f'num = {num}')
    r = sol.findComplement(num)
    print(f'r = {r}')
    print('==========================')

