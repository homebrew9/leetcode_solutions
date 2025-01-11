class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # len = odd, first num = odd  => n//2 + 1
        # len = odd, first num = even => n//2
        # len = even, first no. = odd => n//2
        # len = even, first no. = even => n//2
        num_range = high - low + 1
        if num_range % 2 == 1 and low % 2 == 1:
            return num_range//2 + 1
        else:
            return num_range//2

# Main section
for low, high in [
                    (3, 7),
                    (8, 10),
                    (0, 0),
                    (0, 100),
                    (0, 1000000000),
                    (3313, 847363281),
                 ]:
    print(f'low, high = {low}, {high}')
    sol = Solution()
    r = sol.countOdds(low, high)
    print(f'r = {r}')
    print('=================')

