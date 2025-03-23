from typing import List
from collections import defaultdict

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def dfs(node):
            for next_node in hsh[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    dfs(next_node)
        # Number of nodes is N
        N = len(properties)
        hsh = defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                a = properties[i]
                b = properties[j]
                if len(set(a).intersection(set(b))) >= k:
                    hsh[i] += [j]
                    hsh[j] += [i]
        cc_set = set()
        for node in range(N):
            seen = set()
            seen.add(node)
            dfs(node)
            cc_set.add(tuple(sorted(seen)))
        return len(cc_set)

# Main section
for properties, k in [
                        ([[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], 1),
                        ([[1,2,3],[2,3,4],[4,3,5]], 2),
                        ([[1,1],[1,1]], 2),
                     ]:
    print(f'properties, k = {properties}, {k}')
    sol = Solution()
    r = sol.numberOfComponents(properties, k)
    print(f'r = {r}')
    print('===================')

