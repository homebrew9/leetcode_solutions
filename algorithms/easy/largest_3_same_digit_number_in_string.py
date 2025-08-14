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

    def largestGoodInteger_2(self, num: str) -> str:
        N = len(num)
        max_val = -1
        res = ''
        for i in range(N-2):
            chunk = num[i:i+3]
            if len(set(chunk)) == 1 and int(chunk) > max_val:
                max_val = int(chunk)
                res = chunk
        return res

    def largestGoodInteger_3(self, num: str) -> str:
        largest_substring = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                sub = num[i:i+3]
                if sub > largest_substring:
                    largest_substring = sub
        return largest_substring

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
    r2 = sol.largestGoodInteger_2(num)
    r3 = sol.largestGoodInteger_3(num)
    print(f'r   = {r}')
    print(f'r1  = {r1}')
    print(f'r2  = {r2}')
    print(f'r3  = {r3}')
    print('==============================')



