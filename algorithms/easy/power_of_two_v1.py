class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Bit manipulation
        return n > 0 and n & (n-1) == 0

    def isPowerOfTwo_1(self, n: int) -> bool:
        # Another one without using loops/recursion
        return n > 0 and int(bin(n)[2:][::-1]) == 1

    def isPowerOfTwo_2(self, n: int) -> bool:
        return n in {2**n for n in range(31)}

# Main section
for n in [
            65536,
            1610612736,
            1,
            0,
            -256,
         ]:
    print(f'n  = {n}')
    sol = Solution()
    r = sol.isPowerOfTwo(n)
    r1 = sol.isPowerOfTwo_1(n)
    r2 = sol.isPowerOfTwo_2(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('================')







