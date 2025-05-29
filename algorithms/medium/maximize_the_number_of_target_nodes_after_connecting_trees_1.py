from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def bfs(node, hsh1, k):
            if k < 0:
                return 0
            #print(f'\tnode = {node}')
            dq = deque()
            seen = set()
            dq.append(node)
            seen.add(node)
            steps = 0
            total = 0
            while dq:
                #print(f'\t\tdq = {dq}')
                size = len(dq)
                for _ in range(size):
                    curr = dq.popleft()
                    total += 1
                    #print(f'\t\t\tcurr, total = {curr}, {total}')
                    for next_node in hsh1[curr]:
                        if next_node not in seen:
                            seen.add(next_node)
                            dq.append(next_node)
                steps += 1
                if steps >= k+1:
                    break
            return total
        hsh1 = defaultdict(list)
        hsh2 = defaultdict(list)
        for u, v in edges1:
            hsh1[u] += [v]
            hsh1[v] += [u]
        for u, v in edges2:
            hsh2[u] += [v]
            hsh2[v] += [u]
        #print(hsh1)
        #print(hsh2)
        res = list()
        max_val = float('-inf')
        #print('========== edges1 ==========')
        for node in range(len(edges1)+1):
            cnt = bfs(node, hsh1, k)
            #print(f'node, cnt = {node}, {cnt}')
            res.append(cnt)
        #print('========== edges2 ==========')
        for node in range(len(edges2)+1):
            cnt = bfs(node, hsh2, k-1)
            #print(f'node, cnt = {node}, {cnt}')
            max_val = max(max_val, cnt)
        return [i + max_val for i in res]

# Main section
for edges1, edges2, k in [
                            ([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2),
                            ([[0,1],[0,2],[0,3],[0,4]], [[0,1],[1,2],[2,3]], 1),
                         ]:
    print(f'edges1 = {edges1}')
    print(f'edges2 = {edges2}')
    print(f'k = {k}')
    sol = Solution()
    r = sol.maxTargetNodes(edges1, edges2, k)
    print(f'r = {r}')
    print('========================================')



















