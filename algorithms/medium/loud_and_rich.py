from typing import List
from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(node):
            if res[node] is not None:
                return res[node]
            res[node] = node
            for parent_node in hsh[node]:
                candidate = dfs(parent_node)
                if quiet[candidate] < quiet[res[node]]:
                    res[node] = candidate
            return res[node]

        N = len(quiet)
        res = [None for i in range(N)]
        hsh = defaultdict(list)
        for a, b in richer:
            hsh[b] += [a]
        key_list = list(hsh.keys())
        for k in key_list:
            dfs(k)
        res1 = [i if res[i] is None else res[i] for i in range(N)]
        return res1

# Main section
for richer, quiet in [
                        ([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]),
                        ([], [0]),
                     ]:
    print(f'richer = {richer}')
    print(f'quiet = {quiet}')
    sol = Solution()
    r = sol.loudAndRich(richer, quiet)
    print(f'r = {r}')
    print('=====================')




