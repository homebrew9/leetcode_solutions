class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up, down, left, right = 0, 0, 0, 0
        for m in moves:
            if m == 'U': up += 1
            elif m == 'D': down += 1
            elif m == 'L': left += 1
            elif m == 'R': right += 1
        return up == down and left == right

# Main section
for moves in [
                'UD',
                'LL',
                'UDDUURLRLLRRUDUDLLRLURLRLRLUUDLULRULRLDDDUDDDDLRRDDRDRLRLURRLLRUDURULULRDRDLURLUDRRLRLDDLUUULUDUUUUL',
             ]:
    print(f'moves = {moves}')
    sol = Solution()
    r = sol.judgeCircle(moves)
    print(f'r = {r}')
    print('==================================')


