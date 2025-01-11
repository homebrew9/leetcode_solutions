class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            sum_squares = 0
            while n != 0:
                sum_squares += (n % 10)**2
                n = n // 10
            return sum_squares

        if n == 1:
            return True
        hsh_seen = dict()
        while True:
            n = sum_of_squares(n)
            print(f'\t>>> {n}')
            if n == 1:
                return True
            if n in hsh_seen:
                return False
            hsh_seen[n] = 1

# Main section
sol = Solution()
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            13,
            23,
            67,
            123,
            456,
            799,
            1500,
            2457,
            8940,
            10000,
            821839185,
            2147483647,
         ]:
    print(f'n = {n}')
    r = sol.isHappy(n)
    print(f'r = {r}')
    print('=================================')

