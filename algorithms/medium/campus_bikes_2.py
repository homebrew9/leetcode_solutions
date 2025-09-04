from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        dic = {}
        def helper(a,b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        def dfs(p, arr):
            if p == len(workers):
                return 0
            if (p, tuple(arr)) in dic:
                return dic[(p, tuple(arr))]
            temp = float('inf')
            for i in range(len(arr)):
                if arr[i] == 0:
                    temp = min(temp,  helper(bikes[i], workers[p]) + dfs(p + 1, arr[:i] + [1] + arr[i + 1:]))
            dic[(p, tuple(arr))] = temp
            return temp
        
        ans = dfs(0, [0 for _ in range(len(bikes))])
        return int(ans)

# Main section
for workers, bikes in [
                         ([[0,0],[2,1]], [[1,2],[3,3]]),
                         ([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]),
                         ([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]),
                      ]:
    print(f'workers = {workers}')
    print(f'bikes   = {bikes}')
    sol = Solution()
    r = sol.assignBikes(workers, bikes)
    print(f'r       = {r}')
    print('========================')












