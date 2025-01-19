from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        n = 0
        directions = [x, -x, y, -y]
        dq = deque()
        seen = set()
        dq.append(n)
        seen.add(n)
        while dq:
            #print(dq)
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                if curr == target:
                    return True
                for step in directions:
                    cnew = curr + step
                    if cnew < 0 or cnew > x + y:
                        continue
                    if cnew not in seen:
                        seen.add(cnew)
                        dq.append(cnew)
        return False

# Main section
for x, y, target in [
                       (3, 5, 4),
                       (2, 6, 5),
                       (1, 2, 3),
                    ]:
    print(f'x, y = {x}, {y}')
    sol = Solution()
    r = sol.canMeasureWater(x, y, target)
    print(f'r = {r}')
    print('===============')

