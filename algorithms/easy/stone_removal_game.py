class Solution:
    def canAliceWin(self, n: int) -> bool:
        turns = 0
        delta = 10
        while n >= delta:
            n -= delta
            delta -= 1
            turns += 1
        return turns % 2 == 1

# Main section
for n in [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            15, 20, 25, 30, 37, 40, 43, 47, 48, 49, 50,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.canAliceWin(n)
    print(f'r = {r}')
    print('===============')
