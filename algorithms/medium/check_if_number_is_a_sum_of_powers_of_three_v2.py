#
# Yet another iterative solution.
#
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Note that 3^14 < 10^7 < 3^15
        # So we can iterate through a list of powers of 3
        powers = list()
        for k in range(0, 15):
            powers.append(3**k)
        # [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969]
        N = len(powers)
        i = N - 1
        while i >= 0:
            if n - powers[i] >= 0:
                n -= powers[i]
            i -= 1
        return n == 0
            
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

