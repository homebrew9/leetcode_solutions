from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        num, j = 0, 0
        for i, v in enumerate(g):
            if s[j] >= v:
                num += 1
                j += 1
                if j >= len(s):
                    break
            else:
                while j < len(s) and s[j] < v:
                    j += 1
                if j == len(s):
                    break
                else:
                    num += 1
                    j += 1
        return num

# Main section
for g, s in [
               ([1,2,3], [1,1]),
               ([1,2], [1,2,3]),
               ([1,2,3,4], [3,4,5,6]),
               ([8,9,10], [1,1,2,8,8]),
               ([8,9,10], [1,1,2,5,6,7]),
               ([1,2,3], []),
               ([1,2,3], [3]),
            ]:
    sol = Solution()
    print(f'g = {g}, s = {s}')
    r = sol.findContentChildren(g, s)
    print(f'r = {r}')
    print('==========================')

