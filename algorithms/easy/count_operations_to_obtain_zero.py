class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def solve(num1, num2):
            if num1 == 0 or num2 == 0:
                return 0
            if num1 >= num2:
                return 1 + solve(num1 - num2, num2)
            return 1 + solve(num1, num2 - num1)
        res = solve(num1, num2)
        return res

# Main section
for num1, num2 in [
                     (2, 3),
                     (10, 10),
                  ]:
    print(f'num1, num2 = {num1}, {num2}')
    sol = Solution()
    r = sol.countOperations(num1, num2)
    print(f'r = {r}')
    print('=====================')





