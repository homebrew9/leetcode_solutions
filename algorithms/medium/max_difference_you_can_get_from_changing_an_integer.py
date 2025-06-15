class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        a, b = 0, 999_999_999
        for i in '0123456789':
            tmp = int(s.replace(i, '9'))
            a = max(a, tmp)
        for i in '0123456789':
            tmp = int(s.replace(i, '0'))
            if tmp == 0 or len(str(tmp)) < len(s):
                tmp1 = int(s.replace(i, '1'))
                b = min(b, tmp1)
            else:
                b = min(b, tmp)
        return a - b

# Main section
for num in [
              555,
              9,
              100000000,
              1,
              94848847,
              10101928,
              22292392,
              90483784,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.maxDiff(num)
    print(f'r   = {r}')
    print('===================')

