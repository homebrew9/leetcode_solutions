class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Iterative solution
        while n > 0:
            if n % 3 == 0:
                n //= 3
            elif (n - 1) % 3 == 0:
                n -= 1
            else:
                return False
        return True

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

