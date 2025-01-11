# This was asked in the Weekly Contest 350. The wording was a bit vague and
# it resulted in a few WA's. The method below is based on the way it was
# described in the examples.
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank < 5:
            return mainTank * 10
        res = 0
        while mainTank >= 5 and additionalTank >= 1:
            mainTank = (mainTank - 5 + 1)
            res += 50
            additionalTank -= 1
        res += mainTank * 10
        return res

# Main section
for mainTank, additionalTank in [
                                   (5, 10),
                                   (1, 2),
                                   (9, 1),
                                   (9, 2),
                                   (9, 3),
                                   (13, 3),
                                ]:
    print(f'mainTank, additionalTank = {mainTank}, {additionalTank}')
    sol = Solution()
    r = sol.distanceTraveled(mainTank, additionalTank)
    print(f'r = {r}')
    print('===================')

