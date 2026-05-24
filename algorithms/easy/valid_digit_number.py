class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        is_present = False
        q, r = None, None
        while n > 0:
            q, r = divmod(n, 10)
            if r == x:
                is_present = True
            n = q
        return is_present and r != x

# Main section
for n, x in [
               (101, 0),
               (232, 2),
               (5, 1),
            ]:
    print(f'n, x = {n}, {x}')
    sol = Solution()
    r = sol.validDigit(n, x)
    print(f'r = {r}')
    print('==================================')







