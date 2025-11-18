from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Intuition: If a ghost can intercept me in time t then it can reach the
        # target in time t1 <= t. This can be proved; try it with pen and paper.
        # Thus, I only have to check that I can reach the target before any ghost.
        tr, tc = target
        my_distance = abs(tr - 0) + abs(tc - 0)
        for gr, gc in ghosts:
            ghost_dist = abs(gr - tr) + abs(gc - tc)
            if ghost_dist <= my_distance:
                return False
        return True

    def escapeGhosts_1(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return all([abs(gr - target[0]) + abs(gc - target[1]) > abs(target[0]) + abs(target[1]) for gr, gc in ghosts])

# Main section
for ghosts, target in [
                         ([[1,0],[0,3]], [0,1]),
                         ([[1,0]], [2,0]),
                         ([[2,0]], [1,0]),
                      ]:
    print(f'ghosts, target = {ghosts}, {target}')
    sol = Solution()
    r = sol.escapeGhosts(ghosts, target)
    r1 = sol.escapeGhosts_1(ghosts, target)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=====================')



