#
# Binary Search, then simple min from the remaining valid indexes.
# Can also be solved using Monotonic Stack or Heaps. Check those next.
#
from typing import List
import bisect

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        N = len(heights)
        arr = sorted([(v, i) for i, v in enumerate(heights)])
        #print(arr)
        vals = [x[0] for x in arr]
        inds = [x[1] for x in arr]
        res = list()
        for a, b in queries:
            #print(a, b)
            if a == b:
                res.append(a)
            elif b > a and heights[b] > heights[a]:
                res.append(b)
            elif a > b and heights[a] > heights[b]:
                res.append(a)
            else:
                i = bisect.bisect_left(vals, max(heights[a], heights[b]) + 1)
                #print(f'\ti = {i}')
                if i >= N:
                    res.append(-1)
                else:
                    valid_inds = [x for x in inds[i:] if x > max(a, b)]
                    if len(valid_inds) == 0:
                        res.append(-1)
                    else:
                        min_ind = min(valid_inds)
                        res.append(min_ind)
        return res

# Main section
for heights, queries in [
                           ([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]),
                           ([5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]]),
                           ([1,2], [[0,0],[0,1],[1,0],[1,1]]),
                           ([2,3,1], [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]),
                        ]:
    print(f'heights, queries = {heights}, {queries}')
    sol = Solution()
    r = sol.leftmostBuildingQueries(heights, queries)
    print(f'r = {r}')
    print('===================')


