class Solution:
    def integerBreak(self, n: int) -> int:
        # We want to take out as many 3s as possible, but only if the
        # number is > 4. If number is 4, then we should split into (2,2)
        # and not (3,1).
        if n <= 3:
            return n-1
        prd = 1
        while n > 4:
            n -= 3
            prd *= 3
        # At this point n <= 4
        # If n = 4, we split it into (2,2) or just return 4 (the product)
        # If n = 3 or 2, we keep it as it is (don't split it)
        prd *= n
        return prd


# Main section
for n in [
            2, 5, 10, 15, 20, 25, 30,
            35, 40, 45, 50, 55, 58,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.integerBreak(n)
    print(f'r = {r}')
    print('==================')



