class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n != 0:
            hw += n % 2
            n //= 2
        return hw

    def hammingWeight_rec(self, n: int, hw: int) -> int:
        # If hw is declared as a global variable or a class member, then it
        # need not be passed as a parameter.
        # Actually, we CAN simply pass n as parameter and calculate HW - see
        # next program: "number_of_1_bits_v2.py"
        if n == 0:
            return hw
        hw += n % 2
        return self.hammingWeight_rec(n//2, hw)

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
    r1 = sol.hammingWeight(n)
    r2 = sol.hammingWeight_rec(n, 0)
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('===========================')


