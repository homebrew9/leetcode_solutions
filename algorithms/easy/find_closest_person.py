class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(z - x)   # Person 1
        dist2 = abs(z - y)   # Person 2
        if dist1 == dist2:
            return 0
        if dist1 < dist2:
            return 1
        return 2

# Main section
for x, y, z in [
                  (2, 7, 4),
                  (2, 5, 6),
                  (1, 5, 3),
               ]:
    print(f'x, y, z = {x}, {y}, {z}')
    sol = Solution()
    r = sol.findClosest(x, y, z)
    print(f'r = {r}')
    print('========================')

