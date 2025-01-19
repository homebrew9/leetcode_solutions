from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        N = len(s)
        net_shift = 0
        for direction, amount in shift:
            if direction == 1:
                net_shift += amount % N
            elif direction == 0:
                net_shift -= amount % N
        if net_shift > 0:
            net_shift = net_shift % N
            return s[-net_shift:] + s[:-net_shift]
        if net_shift < 0:
            net_shift = abs(net_shift) % N
            return s[net_shift:] + s[:net_shift]
        return s

# Main section
for s, shift in [
                   ('abc', [[0,1],[1,2]]),
                   ('abcdefg', [[1,1],[1,1],[0,2],[1,3]]),
                   ('abc', [[0,4]]),
                   ('abcd', [[0,100],[1,100],[0,50],[1,50]]),
                   ('xqgwkiqpif', [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]),
                ]:
    print(f's, shift = {s}, {shift}')
    sol = Solution()
    r = sol.stringShift(s, shift)
    print(f'r = {r}')
    print('===================')


