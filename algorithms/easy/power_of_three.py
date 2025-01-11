class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

# Main section
sol = Solution()
for n in [
            -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 59049, 59099, -59049, -59099, 1162261467, -1162261467, 1162261999
         ]:
    print(f'n = {n}')
    r = sol.isPowerOfThree(n)
    print(f'r = {r}')
    print('===========================')


