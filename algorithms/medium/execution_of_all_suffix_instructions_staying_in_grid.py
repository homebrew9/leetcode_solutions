from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        hsh = {'L': [0,-1], 'R': [0,1], 'U': [-1,0], 'D': [1,0]}
        res = list()
        for i in range(len(s)):
            #print(f'i, res = {i}, {res}')
            x, y = startPos
            cnt = 0
            off_grid = False
            for j in range(i, len(s)):
                #print(f'\tj, res = {j}, {res}')
                ch = s[j]
                x, y = x + hsh[ch][0], y + hsh[ch][1]
                if 0 <= x < n and 0 <= y < n:
                    cnt += 1
                else:
                    off_grid = True
                    res.append(cnt)
                    break
            if not off_grid:
                res.append(cnt)
        return res

# Main section
for n, startPos, s in [
                         (3, [0,1], 'RRDDLU'),
                         (2, [1,1], 'LURD'),
                         (1, [0,0], 'LRUD'),
                      ]:
    print(f'n, startPos, s = {n}, {startPos}, {s}')
    sol = Solution()
    r = sol.executeInstructions(n, startPos, s)
    print(f'r = {r}')
    print('====================')

