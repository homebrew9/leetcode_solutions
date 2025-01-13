"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #def dfs(node):
        #    if node in self.seen:
        #        return
        #    self.seen.add(node)
        #    for nb in node.neighbors:
        #        self.hsh[node.val] += [nb.val]
        #        dfs(nb)
        def dfs(node):
            # All DFS is iterative, using stacks
            stack = list()
            seen = set()
            stack.append(node)
            seen.add(node)
            while stack:
                cur = stack.pop()
                for nb in cur.neighbors:
                    self.hsh[cur.val] += [nb.val]
                    if nb not in seen:
                        seen.add(nb)
                        stack.append(nb)
        def clone(val):
            stack = list()
            created = set()
            track = dict()
            nd = Node(val)
            stack.append(val)
            created.add(val)
            track[val] = nd
            while stack:
                cur = stack.pop()
                nd1 = track[cur]
                for x in self.hsh[cur]:
                    if x not in created:
                        created.add(x)
                        stack.append(x)
                        track[x] = Node(x)
                    nd1.neighbors += [track[x]]
            return nd
        if node is None:
            return node
        self.hsh = defaultdict(list)
        self.seen = set()
        dfs(node)
        #print(self.hsh)
        return clone(node.val)

'''
[[2,4],[1,3],[2,4],[1,3]]
[]
[[]]
[[2,3],[1,4],[1,4,5],[2,3,6],[3,6,7],[4,5,7],[5,6]]
'''

