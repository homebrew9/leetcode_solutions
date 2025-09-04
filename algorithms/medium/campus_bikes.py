from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        N = len(workers)
        M = len(bikes)
        arr = list()
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx-bx) + abs(wy-by)
                arr.append((dist, i, j))
        arr.sort()
        worker_status = [-1 for _ in range(N)]
        bikes_status = [False for _ in range(M)]
        pair_count = 0
        for d, w, b in arr:
            if worker_status[w] == -1 and not bikes_status[b]:
                worker_status[w] = b
                bikes_status[b] = True
                pair_count += 1
                if pair_count == N:
                    #return worker_status
                    break
        return worker_status # Pylance on VSCode does not like a return inside "for" loop / non-return last statement.

# Main section
for workers, bikes in [
                         ([[0,0],[2,1]], [[1,2],[3,3]]),
                         ([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]),
                      ]:
    print(f'workers = {workers}')
    print(f'bikes   = {bikes}')
    sol = Solution()
    r = sol.assignBikes(workers, bikes)
    print(f'r       = {r}')
    print('========================')




















