#
# Does not work for last test case. The next points should converge towards (1,1).
#
from collections import defaultdict

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        hsh = defaultdict(int)
        def traverse(x, y):
            print(f'\tx, y, hsh = {x}, {y}, {hsh}')
            if x == 1 and y == 1:
                return True
            elif x % 2 == 0:
                k = (x//2, y)
                if k in hsh:
                    return False
                hsh[k] += 1
                return traverse(x//2, y)
            elif y % 2 == 0:
                k = (x, y//2)
                if k in hsh:
                    return False
                hsh[k] += 1
                return traverse(x, y//2)
            elif y % 2 == 1:
                k = (x, y+x)
                if k in hsh:
                    return False
                hsh[k] += 1
                return traverse(x, y+x)
            else:
                k = (x+y, y)
                if k in hsh:
                    return False
                hsh[k] += 1
                return traverse(x+y, y)
            return False

        return traverse(targetX, targetY)

# Main section
for targetX, targetY in [
                           (4, 7),
                           (6, 9),
                           (10000, 10000),
                           (3, 7),
                        ]:
    print(f'targetX, targetY = {targetX}, {targetY}')
    sol = Solution()
    r = sol.isReachable(targetX, targetY)
    print(f'r = {r}')
    print('===================')

