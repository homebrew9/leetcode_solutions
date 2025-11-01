class Solution:
    def totalMoney(self, n: int) -> int:
        # Week # 1 = [1,2,3,4,5,6,7]
        # Week # 2 = [2,3,4,5,6,7,8]
        # Week # 3 = [3,4,5,6,7,8,9]
        # All of them are arithmetic series with a = 1,2,3,... n = 7 or less, and d = 1
        # Sum of n terms of arithmetic series = (n/2)*(2a + (n-1)d)
        weeks, days = divmod(n, 7)
        res = 0
        a = 1
        for _ in range(weeks):
            res += 7 * (a + 3)
            a += 1
        res += (days * (2*a + (days - 1))) // 2
        return res

    def totalMoney_1(self, n: int) -> int:
        # Week # 1 = [1,2,3,4,5,6,7]         = 28 + 0*7
        # Week # 2 =   [2,3,4,5,6,7,8]       = 28 + (8-1) = 28 + 1*7
        # Week # 3 =      [3,4,5,6,7,8,9]    = (28 + 1*7) + (9-2) = 28 + 2*7
        # Total for all weeks = 28*w + (1+2+...+w-1)*7
        # To calculate money on the additional days, note that it is an
        # arithmetic series (w+1)...(w+d) i.e. S(w+d) - S(w+1)
        # All of them are arithmetic series with a = 1,2,3,... n = 7 or less, and d = 1
        # Sum of n terms of arithmetic series = (n/2)*(2a + (n-1)d)
        res = 0
        weeks, days = divmod(n, 7)
        res += 28 * weeks + ((weeks * (weeks - 1))//2) * 7
        res += ((weeks + days) * (weeks + days + 1))//2 - (weeks * (weeks + 1))//2
        return res

    def totalMoney_2(self, n: int) -> int:
        w, d = divmod(n, 7)
        res = 28 * w + ((w * (w - 1))//2) * 7 + ((w + d) * (w + d + 1))//2 - (w * (w + 1))//2
        return res

    def totalMoney_3(self, n: int) -> int:
        w, d = divmod(n, 7)
        res = (7 * w * (w + 7))//2 + (d * (d + 2*w + 1))//2
        return res

    def totalMoney_4(self, n: int) -> int:
        w, d = divmod(n, 7)
        res = (w * (6 * w + 49) + (d + w)**2 + d)//2
        return res

    def totalMoney_5(self, n: int) -> int:
        w, d = divmod(n, 7)
        res = (6 * (w + 4)**2 + (w + d)**2 + (w + d - 96))//2
        return res

# Main section
for n in [
            4,
            10,
            20,
         ]:
    print(f'n  = {n}')
    sol = Solution()
    r = sol.totalMoney(n)
    r1 = sol.totalMoney_1(n)
    r2 = sol.totalMoney_2(n)
    r3 = sol.totalMoney_3(n)
    r4 = sol.totalMoney_4(n)
    r5 = sol.totalMoney_5(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r3 = {r3}')
    print(f'r4 = {r4}')
    print(f'r5 = {r5}')
    print('=====================')



