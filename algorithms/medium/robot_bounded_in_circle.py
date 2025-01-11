class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        face = {('N', 'L'): 'W', ('N', 'R'): 'E',
                ('S', 'L'): 'E', ('S', 'R'): 'W',
                ('E', 'L'): 'N', ('E', 'R'): 'S',
                ('W', 'L'): 'S', ('W', 'R'): 'N'
               }
        walk = {'N': (0,1), 'E': (1,0), 'W': (-1,0), 'S': (0,-1)}
        # A travel vector comprises of location co-ordinates and the direction
        # that the robot is facing.
        vector = [0, 0, 'N']
        for i in instructions:
            x, y, d = vector
            if i == 'G':
                vector = [x + walk[d][0], y + walk[d][1], d]
            else:
                vector = [x, y, face[(d, i)]]
        # After all instructions are followed, if the robot has come full circle
        # or is facing any direction other than North, then it will keep going
        # in circles! Note that if the final direction of the robot is North,
        # then it will NOT keep traveling in circles!
        x, y, d = vector
        if (x == 0 and y == 0) or (d != 'N'):
            return True
        return False

# Main section
for instructions in [
                       'GGLLGG',
                       'GG',
                       'GL',
                       'LGLGLG',
                       'LGLGLGL',
                    ]:
    print(f'instructions = {instructions}')
    sol = Solution()
    r = sol.isRobotBounded(instructions)
    print(f'r = {r}')
    print('==================')

