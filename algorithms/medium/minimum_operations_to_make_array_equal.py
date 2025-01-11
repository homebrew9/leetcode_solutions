class Solution:
    def minOperations(self, n: int) -> int:
        # n = 2, arr = [1,3],                res = 1
        # n = 4, arr = [1,3,5,7],            res = 1+3 = 4
        # n = 6, arr = [1,3,5,7,9,11],       res = 1+3+5 = 9
        # n = 8, arr = [1,3,5,7,9,11,13,15], res = 1+3+5+7 = 16  = (n//2)**2 = k^2 where k = n//2
        # ==========
        # n = 3, arr = [1,3,5]                  res = 2
        # n = 5, arr = [1,3,5,7,9],             res = 2+4 = 6
        # n = 7, arr = [1,3,5,7,9,11,13],       res = 2+4+6 = 12
        # n = 9, arr = [1,3,5,7,9,11,13,15,17], res = 2+4+6+8 = 20  = 2*(1+2+3+...+n//2) = k*(k+1) where k = n//2
        # ===========
        k = n//2
        if n % 2 == 1:
            return k * (k + 1)
        else:
            return k * k

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            10,
            1000,
            278,
            807,
            3498,
            9876,
            10000
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.minOperations(n)
    print(f'r = {r}')
    print('====================')

