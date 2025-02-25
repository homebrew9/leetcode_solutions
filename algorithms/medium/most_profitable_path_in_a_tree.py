from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs_bob(node):
            if node == 0:
                self.bob_path = bob_arr[:]
                return
            for next_node in hsh[node]:
                if next_node not in bob_set:
                    bob_set.add(next_node)
                    bob_arr.append(next_node)
                    dfs_bob(next_node)
                    bob_arr.pop()
                    bob_set.remove(next_node)
        def dfs_alice(node):
            if node in leaf_nodes:
                arr1 = alice_arr[:]
                total = 0
                for i, v in enumerate(arr1):
                    if v not in bob_hsh or i < bob_hsh[v]:
                        total += amount[v]
                    elif i == bob_hsh[v]:
                        total += amount[v] // 2
                self.res = max(self.res, total)
                return
            for next_node in hsh[node]:
                if next_node not in alice_set:
                    alice_set.add(next_node)
                    alice_arr.append(next_node)
                    dfs_alice(next_node)
                    alice_arr.pop()
                    alice_set.remove(next_node)
        hsh = defaultdict(list)
        for u, v in edges:
            hsh[u] += [v]
            hsh[v] += [u]
        bob_set = set()
        self.bob_path = list()
        bob_arr = list()
        bob_arr.append(bob)
        bob_set.add(bob)
        dfs_bob(bob)
        bob_hsh = {v: i for i, v in enumerate(self.bob_path)}
        leaf_nodes = set()
        for k, v in hsh.items():
            if len(v) == 1 and k != 0:
                leaf_nodes.add(k)
        self.res = float('-inf')
        alice_arr = list()
        alice_set = set()
        alice_set.add(0)
        alice_arr.append(0)
        dfs_alice(0)
        return self.res

# Main section
for edges, bob, amount, ans in [
                                  ([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6], 6),
                                  ([[0,1]], 1, [-7280,2350], -7280),
                                  ([[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], 4, [2,2,2,2,2,2,2,2], 11),
                                  ([[0,2],[0,5],[1,3],[1,5],[2,4]], 4, [5018,8388,6224,3466,3808,3456], 20328),
                               ]:
    print(f'edges, bob, amount = {edges}, {bob}, {amount}')
    sol = Solution()
    r = sol.mostProfitablePath(edges, bob, amount)
    print(f'r = {r}')
    assert(r == ans)
    print('==========================')

