class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def traverse(x, y):
            print(f'\tx, y = {x}, {y}')
            if x == 1 and y == 1:
                return True
            elif x % 2 == 0:
                return traverse(x//2, y)
            elif y % 2 == 0:
                return traverse(x, y//2)
            elif x > y:
                return traverse(x + y, y)  # x - y works as well
            elif y > x:
                return traverse(x, y + x)  # y - x works as well
            else:
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


