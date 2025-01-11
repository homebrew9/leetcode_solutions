class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        return (n % 2) + self.hammingWeight(n//2)

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



