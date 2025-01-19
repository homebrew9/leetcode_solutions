#
# Wrong logic! Does not return the *minimum* moves!
# The answer for the last testcase (3rd one) is 1 but this algorithm returns 3.
#

from typing import List
from collections import deque

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        def is_empty(board):
            for r in range(N):
                for c in range(N):
                    if board[r][c] == 1:
                        return False
            return True
        def bfs(r, c, board):
            dq = deque()
            seen = set()
            dq.append((r, c))
            seen.add((r, c))
            steps = 0
            while dq:
                size = len(dq)
                for _ in range(size):
                    row, col = dq.popleft()
                    if board[row][col] == 1:
                        board[row][col] = 0
                        return (steps, board)
                    for dr, dc in directions:
                        rnew = row + dr
                        cnew = col + dc
                        if (0 <= rnew < N) and (0 <= cnew < N) and (rnew, cnew) not in seen:
                            seen.add((rnew, cnew))
                            dq.append((rnew, cnew))
                steps += 1
        N = len(rooks)
        board = [[0 for _ in range(N)] for _ in range(N)]
        res = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        for r, c in rooks:
            board[r][c] = 1
        for i in range(N):
            # BFS from the diagonal
            steps, board = bfs(i, i, board)
            res += steps
            if is_empty(board):
                break
        return res

# Main section
for rooks in [
                #[[0,0],[1,0],[1,1]],
                #[[0,0],[0,1],[0,2],[0,3]],
                [[0,1],[1,2],[2,1],[3,3]],
             ]:
    print(f'rooks = {rooks}')
    sol = Solution()
    r = sol.minMoves(rooks)
    print(f'r = {r}')
    print('====================')


