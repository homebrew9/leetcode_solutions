class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Recursive solution
        def solve(n):
            if n == 0:
                return True
            if n % 3 == 0:
                return solve(n//3)
            elif (n-1) % 3 == 0:
                return solve(n-1)
            else:
                return False
        return solve(n)

# Main section
for n in [
            12,
            91,
            21,
            6902878,
            29524,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.checkPowersOfThree(n)
    print(f'r = {r}')
    print('=========================')

