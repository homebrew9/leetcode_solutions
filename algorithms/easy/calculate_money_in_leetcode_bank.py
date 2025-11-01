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

# Main section
for n in [
            4,
            10,
            20,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.totalMoney(n)
    print(f'r = {r}')
    print('=====================')

































