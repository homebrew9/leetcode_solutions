# ================================================================================
# The hints were really helpful. Trying to change each element of delta array
# results in TLE.
# Hint 1: Instead of shifting every character in each shift, could you keep
#     track of which characters are shifted and by how much across all shifts?
# Hint 2: Try marking the start and ends of each shift, then perform a
#     prefix sum of the shifts.
# ================================================================================
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        # The "delta" array marks the start and end indices of the movement
        # and its reverse. The prefix sum then calculates the net total movement.
        delta = [0 for _ in range(N)]
        for start, end, direction in shifts:
            if direction == 0:
                delta[start] -= 1
                if end + 1 < N:
                    delta[end + 1] += 1
            elif direction == 1:
                delta[start] += 1
                if end + 1 < N:
                    delta[end + 1] -= 1
        #print(delta)
        chars = list(s)
        for i in range(N):
            if i == 0:
                d = delta[0]
            else:
                d = delta[i-1] + delta[i]
            c = chars[i]
            new_ord = ord(c) + (d % 26)
            if new_ord > 122:
                new_ord = new_ord - 122 + 97 - 1
            chars[i] = chr(new_ord)
            delta[i] = d
        return ''.join(chars)

# Main section
for s, shifts in [
                    ('abc', [[0,1,0],[1,2,1],[0,2,1]]),
                    ('dztz', [[0,0,0],[1,1,1]]),
                 ]:
    print(f's, shifts = {s}, {shifts}')
    sol = Solution()
    r = sol.shiftingLetters(s, shifts)
    print(f'r = {r}')
    print('====================')


