class Solution:
    def coloredCells(self, n: int) -> int:
        '''
              1 +  0 =  1
              1 +  4 =  5
              5 +  8 = 13
             13 + 12 = 25
             25 + 16 = 41
             F(n) = F(n-1) + 4 * (n - 1)
             F(1) = 1
        '''
        # Iterative solution
        res = 1
        for i in range(2, n + 1):
            res = res + 4*(i - 1)
        return res

# Main section
for n in [
                 1,
                 2,
                10,
                53,
               100,
               781,
              1000,
              3599,
             98301,
            100000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.coloredCells(n)
    print(f'r = {r}')
    print('================================')

