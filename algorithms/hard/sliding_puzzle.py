#
# Do a BFS with the board as the starting node and all next configs as the next nodes
# with the edge length being 1.
#
from typing import List
from collections import deque
from copy import deepcopy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def get_next_config(board):
            rows, cols = 2, 3
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            next_config_list = list()
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == 0:
                        for dr, dc in directions:
                            rnew = r + dr
                            cnew = c + dc
                            if 0 <= rnew < rows and 0 <= cnew < cols:
                                tmp = deepcopy(board)
                                tmp[r][c], tmp[rnew][cnew] = tmp[rnew][cnew], tmp[r][c]
                                next_config_list.append(tmp)
            return next_config_list
        def list_to_tuple(board):
            return tuple([tuple(x) for x in board])
        target = [[1,2,3],[4,5,0]]
        dq = deque()
        seen = set()
        dq.append(board)
        seen.add(list_to_tuple(board))
        steps = 0
        while dq:
            #print(dq)
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                #print(f'\t{steps}, {curr}')
                if curr == target:
                    #print(f'\t\tInside curr == target; curr={curr}, target={target}')
                    return steps
                next_config_list = get_next_config(curr)
                for config in next_config_list:
                    if (tpl := list_to_tuple(config)) not in seen:
                        dq.append(config)
                        seen.add(tpl)
            steps += 1
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


