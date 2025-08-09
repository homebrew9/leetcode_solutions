class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Bit manipulation
        return n > 0 and n & (n-1) == 0

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

















