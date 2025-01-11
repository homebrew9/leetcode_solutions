class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n /= 4
        return True

# Main section
sol = Solution()
for n in [
            16,
            1,
            16777216,
            1048576,
            16384,
            1073741824,
            262144,
            4194304,
            67108864,
            5,
            93,
            163845,
            16777215,
            1073748824,
            -1073748824,
            0,
            -999,
         ]:
    print(f'n = {n}')
    r = sol.isPowerOfFour(n)
    print(f'r = {r}')
    print('======================')

