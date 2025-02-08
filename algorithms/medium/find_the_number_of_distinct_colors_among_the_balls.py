from typing import List
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hsh_ball = defaultdict(int)
        hsh_color = defaultdict(set)
        res = list()
        cnt = 0
        for ball, color in queries:
            if ball in hsh_ball:
                c = hsh_ball[ball]
                hsh_color[c].remove(ball)
                if len(hsh_color[c]) == 0:
                    del hsh_color[c]
                hsh_color[color].add(ball)
                hsh_ball[ball] = color
            elif color in hsh_color:
                hsh_color[color].add(ball)
                hsh_ball[ball] = color
            else:
                hsh_color[color].add(ball)
                hsh_ball[ball] = color
            res.append(len(hsh_color))
        return res

# Main section
for limit, queries in [
                         (4, [[1,4],[2,5],[1,3],[3,4]]),
                         (4, [[0,1],[1,2],[2,2],[3,4],[4,5]]),
                         (1, [[0,6],[1,6],[0,7],[0,9],[1,7]]),
                         (1, [[0,1],[0,4],[1,2],[1,5],[1,4]]),
                      ]:
    print(f'limit, queries = {limit}, {queries}')
    sol = Solution()
    r = sol.queryResults(limit, queries)
    print(f'r = {r}')
    print('======================')

