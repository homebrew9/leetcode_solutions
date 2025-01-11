class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        i = 0
        p = (1<<i) - n
        while p < 0:
            i += 1
            p = (1<<i) - n
        if p == 0:
            return True
        else:
            return False

# Main section
for n in [
            65536,
            1610612736,
            1,
            0,
            -256,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.isPowerOfTwo(n)
    print(f'r = {r}')
    print('================')

