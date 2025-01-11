from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cnt = 0
        start, end = 0, 0
        prev = None
        arr = list()
        for i, ch in enumerate(s):
            if i == 0:
                start, end = i, i
                cnt += 1
            elif ch == prev:
                end = i
                cnt += 1
            else:
                if cnt >= 3:
                    arr.append([start, end])
                cnt = 1
                start, end = i, i
            prev = ch
        if cnt >= 3:
            arr.append([start, end])
        return arr

# Main section
for s in [
            'abbxxxxzzy',
            'abc',
            'abcdddeeeeaabbbcd',
            'a',
            'aa',
            'aaa',
            'aab',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.largeGroupPositions(s)
    print(f'r = {r}')
    print('=================')

