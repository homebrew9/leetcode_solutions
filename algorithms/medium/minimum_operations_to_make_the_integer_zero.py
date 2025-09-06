class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1

# Main section
for num1, num2 in [
                     (3, -2),
                     (5, 7),
                     (334521, -41),
                     (3451, 2213),
                     (1066381, -2233),
                     (99861952, 12311),
                     (1000000000, 100),
                     (1000000000, -1321),
                  ]:
    print(f'num1, num2 = {num1}, {num2}')
    sol = Solution()
    r = sol.makeTheIntegerZero(num1, num2)
    print(f'r = {r}')
    print('========================')








