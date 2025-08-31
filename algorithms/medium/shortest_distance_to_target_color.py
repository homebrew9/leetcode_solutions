from typing import List

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        NEG_INF = -1
        POS_INF = 50001
        N = len(colors)
        left_pfx = [[NEG_INF, NEG_INF, NEG_INF] for _ in range(N)]
        for i in range(N):
            left_pfx[i][colors[i]-1] = i
            if i > 0:
                for j in range(3):
                    left_pfx[i][j] = max(left_pfx[i-1][j], left_pfx[i][j])
        right_pfx = [[POS_INF, POS_INF, POS_INF] for _ in range(N)]
        for i in range(N-1, -1, -1):
            right_pfx[i][colors[i]-1] = i
            if i < N - 1:
                for j in range(3):
                    right_pfx[i][j] = min(right_pfx[i+1][j], right_pfx[i][j])
        res = list()
        for i, c in queries:
            if left_pfx[i][c-1] == NEG_INF and right_pfx[i][c-1] == POS_INF:
                res.append(-1)
            elif left_pfx[i][c-1] != NEG_INF and right_pfx[i][c-1] != POS_INF:
                val = min(abs(i - left_pfx[i][c-1]), abs(i - right_pfx[i][c-1]))
                res.append(val)
            elif left_pfx[i][c-1] == NEG_INF:
                val = abs(i - right_pfx[i][c-1])
                res.append(val)
            elif right_pfx[i][c-1] == POS_INF:
                val = abs(i - left_pfx[i][c-1])
                res.append(val)
        return res

# Main section
for colors, queries in [
                          ([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]),
                          ([1,2], [[0,3]]),
                       ]:
    print(f'colors  = {colors}')
    print(f'queries = {queries}')
    sol = Solution()
    r = sol.shortestDistanceColor(colors, queries)
    print(f'r       = {r}')
    print('==========================')


















