class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        for i in range(10):
            s = str(i) * 3
            if s in num:
                res = s
        return res

# Main section
for num in [
              '6777133339',
              '2300019',
              '42352338',
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.largestGoodInteger(num)
    print(f'r   = {r}')
    print('==============================')
















