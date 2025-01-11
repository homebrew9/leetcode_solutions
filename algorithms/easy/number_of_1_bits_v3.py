class Solution:
    def hammingWeight(self, n: int) -> int:
        # Wegner's technique:
        # Consider binary representations of n and (n-1)
        # Subtracting 1 changes the rightmost string of 0s to 1s, and changes the rightmost 1 to a 0.
        # E.g. 15 = 1111, 14 = 1110
        #       8 = 1000,  7 = 0111
        # Hence the operation n & (n-1) zeros out the least significant nonzero bit of n
        # E.g. 15 & 14 = 1111 & 1110 = 1110
        #       8 &  7 = 1000 & 0111 = 0000
        # If n originally had p bits that were 1, then after p iterations of this operation,
        # n will be reduced to 0.
        bitcount = 0
        while n != 0:
            n &= (n - 1)
            bitcount += 1
        return bitcount

# Main section
sol = Solution()
for n in [
            0b00000000000000000000000000001011,
            0b00000000000000000000000010000000,
            0b11111111111111111111111111111101,
            0b11111111111111111111111111111111,
            0b00000000000000000000000000000011,
         ]:
    print(f'n = {bin(n)}')
    r = sol.hammingWeight(n)
    print(f'r = {r}')
    print('===========================')




