class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        for i in range(10):
            s = str(i) * 3
            if s in num:
                res = s
        return res

    def largestGoodInteger_1(self, num: str) -> str:
        for n in range(9, -1, -1):
            v = str(n) * 3
            if v in num:
                return v
        return ''
    

# Main section
for num in [
              '6777133339',
              '2300019',
              '42352338',
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.largestGoodInteger(num)
    r1 = sol.largestGoodInteger_1(num)
    print(f'r   = {r}')
    print(f'r1  = {r1}')
    print('==============================')






