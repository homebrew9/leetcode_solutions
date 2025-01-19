#
# This is the official solution.
#
from typing import List
from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge cases
        if n <= 2:
            return [i for i in range(n)]
        # Build the graph with the adjacency list
        neighbors = [set() for _ in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        print(f'\tneighbors = {neighbors}')
        # Initialize the first layer of leaves
        leaves = list()
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        print(f'\tleaves = {leaves}')
        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        print(f'\tremaining_nodes = {remaining_nodes}')
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            print(f'\t\tremaining_nodes = {remaining_nodes}')
            new_leaves = list()
            # Remove the current leaves along with the edges
            while leaves:
                print(f'\t\t\tleaves = {leaves}')
                leaf = leaves.pop()
                print(f'\t\t\tleaf, neighbors[leaf] = {leaf}, {neighbors[leaf]}')
                # The only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                print(f'\t\t\tneighbor = {neighbor}')
                # Remove the only edge left
                neighbors[neighbor].remove(leaf)
                print(f'\t\t\tneighbors = {neighbors}')
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
                print(f'\t\t\tnew_leaves = {new_leaves}')
                print('=====')
            # Prepare for the next round
            leaves = new_leaves
        # The remaining nodes are the centroids of the graph
        return leaves


# Main section
for n, edges in [
                   (4, [[1,0],[1,2],[1,3]]),
                   #(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.findMinHeightTrees(n, edges)
    print(f'r = {r}')
    print('==================')


