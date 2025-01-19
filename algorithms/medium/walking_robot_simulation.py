# DP Tabulation
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        hsh = {('N',-2):'W', ('N',-1):'E',
               ('S',-2):'E', ('S',-1):'W',
               ('E',-2):'N', ('E',-1):'S',
               ('W',-2):'S', ('W',-1):'N'}
        obs = {(a, b) for a, b in obstacles}
        res = 0
        x, y = 0, 0
        direction = 'N'
        for c in commands:
            if c < 0:
                direction = hsh[(direction, c)]
            else:
                if direction == 'N':
                    for _ in range(c):
                        if (x, y + 1) in obs:
                            break
                        y += 1
                elif direction == 'S':
                    for _ in range(c):
                        if (x, y - 1) in obs:
                            break
                        y -= 1
                elif direction == 'E':
                    for _ in range(c):
                        if (x + 1, y) in obs:
                            break
                        x += 1
                elif direction == 'W':
                    for _ in range(c):
                        if (x - 1, y) in obs:
                            break
                        x -= 1
            res = max(res, x*x + y*y)
        return res

# Main section
for commands, obstacles in [
                             ([4,-1,3], []),
                             ([4,-1,4,-2,4], [[2,4]]),
                             ([6,-1,-1,6], []),
                           ]:
    print(f'commands, obstacles = {commands}, {obstacles}')
    sol = Solution()
    r = sol.robotSim(commands, obstacles)
    print(f'r = {r}')
    print('===================')


