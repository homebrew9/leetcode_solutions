#
# Do a BFS with the board as the starting node and all next configs as the next nodes
# with the edge length being 1.
#
from typing import List
from collections import deque
from copy import deepcopy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def next_config_list(s, i):
            res = list()
            for p in positions[i]:
                arr = list(s)
                arr[i], arr[p] = arr[p], arr[i]
                res.append(''.join(arr))
            return res
        positions = [ [1, 3],
                      [0, 2, 4],
                      [1, 5],
                      [0, 4],
                      [1, 3, 5],
                      [2, 4],
                    ]
        target = '123450'
        s = ''
        for r in range(2):
            s += ''.join([str(n) for n in board[r]])
        dq = deque()
        seen = set()
        dq.append(s)
        seen.add(s)
        moves = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                if curr == target:
                    return moves
                for next_config in next_config_list(curr, curr.index('0')):
                    if next_config not in seen:
                        dq.append(next_config)
                        seen.add(next_config)
            moves += 1
        return -1

# Main section
for board in [
                [[1,2,3],[4,0,5]],
                [[1,2,3],[5,4,0]],
                [[4,1,2],[5,0,3]],
                [[1,2,3],[4,5,0]],
             ]:
    print(f'board = {board}')
    sol = Solution()
    r = sol.slidingPuzzle(board)
    print(f'r = {r}')
    print('==================')


