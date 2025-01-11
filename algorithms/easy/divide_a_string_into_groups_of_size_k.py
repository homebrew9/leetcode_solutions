from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        cnt = 0
        arr = list()
        curr = ''
        for ch in s:
            curr += ch
            cnt += 1
            if cnt == k:
                arr.append(curr)
                curr = ''
                cnt = 0
        if curr != '':
            curr = curr.ljust(k, fill)
            arr.append(curr)
        return arr

# Main section
for s, k, fill in [
                     ('abcdefghi', 3, 'x'),
                     ('abcdefghij', 3, 'x'),
                     ('ctoyjrwtngqwt', 8, 'n'),
                  ]:
    print(f's, k, fill = {s}, {k}, {fill}')
    sol = Solution()
    r = sol.divideString(s, k, fill)
    print(f'r = {r}')
    print('=================')

