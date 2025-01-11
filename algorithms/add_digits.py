class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        while temp >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num = num // 10
            num = temp
        return temp

    def addDigits_opt(self, num: int) -> int:
        return 0 if num == 0 else 9 if num % 9 == 0 else num % 9

# Main solution
sol = Solution()
for num in [
              397,
              2147483647,
              2,
              0,
              1,
              2,
              3,
              4,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
           ]:
    print(f'num = {num}')
    r = sol.addDigits(num)
    print(f'r   = {r}')
    r = sol.addDigits_opt(num)
    print(f'r   = {r}')
    print('============================')

