from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(c, n):
            total = ord(c) + (n%26)
            if total > 122:
                total -= 26
            return chr(total)

        # Update shifts list
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]

        arr = list(s)
        #print(f'\tarr, shifts = {arr}, {shifts}')
        for i in range(len(arr)):
            c = arr[i]
            n = shifts[i]
            arr[i] = shift(c, n)
        return ''.join(arr)

# Main section
for s, shifts in [
                    ('abc', [3,5,9]),
                    ('aaa', [1,2,3]),
                    ('abcdefgh', [12345,28849,39018,23304,18923,67510,22334,78865]),
                 ]:
    print(f's, shifts = {s}, {shifts}')
    sol = Solution()
    r = sol.shiftingLetters(s, shifts)
    print(f'r = {r}')
    print('==========================')

