# This was asked in the Weekly Contest 350. The wording was a bit vague and
# it resulted in a few WA's. The method below is based on the way it was
# described in the examples.
#    Note that the value of the target "x" keeps changing inside the loop
#    so the following is essentially an infinite loop in Java.
#    In Python, if "range" is used in the "for" loop, then its target is
#    fixed, so it will loop through only 5 times, even if x is incremented
#    inside the loop!!! Check the Java program for this problem.
#

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        i = 0
        while i < mainTank:
            i += 1
            if (additionalTank != 0) and (i % 5 == 0):
                additionalTank -= 1
                result += 10
                mainTank += 1
            else:
                result += 10
        return result

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

