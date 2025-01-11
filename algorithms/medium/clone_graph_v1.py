# ==============================================
# DBabichev's solution
# ==============================================
from collections import deque
import pprint

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def print(self):
        print(f'NODE({self.val} : {[n.val for n in self.neighbors]})')


class Solution:
    def createGraph(self, adj):
        hsh = dict()
        for i, lst in enumerate(adj):
            ind = i + 1
            if ind not in hsh:
                hsh[ind] = [Node(ind)]
            node = hsh[ind][0]
            for n in lst:
                if n not in hsh:
                    hsh[n] = [Node(n)]
                #hsh[ind] += [hsh[n][0]]
                node.neighbors.append(hsh[n][0])
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(hsh)
        return hsh[1][0]
    def createAdjList(self, node):
        def bfs(node):
            if node in self.visited:
                return
            self.dq.append(node)
            self.visited.add(node)
            while self.dq:
                size = len(self.dq)
                for i in range(size):
                    cur = self.dq.popleft()
                    if cur.val not in self.hsh:
                        self.hsh[cur.val] = []
                    for n in cur.neighbors:
                        if n not in self.visited:
                            self.dq.append(n)
                            self.visited.add(n)
                        if n.val not in self.hsh:
                            self.hsh[n.val] = []
                        self.hsh[cur.val] += [n.val]
        self.visited = set()
        self.dq = deque()
        self.hsh = dict()
        bfs(node)
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(self.hsh)
        adj = list()
        for k in sorted(self.hsh.keys()):
            adj.append(self.hsh[k])
        return adj
    def cloneGraphOrig(self, node):
        # Clone graph consists of two steps:
        # 1) create an adjacency list by traversing the given graph
        # 2) create another graph from the adjacency list
        adj = self.createAdjList(node)
        node = self.createGraph(adj)
        return node
    def traverseDFS(self, node):
        def dfs(node):
            if node in self.visited:
                return
            #print(f'Visiting => {node.val} : {node}')
            #print(f'Visiting => {node.val}')
            self.nodes.append(str(node.val))
            self.visited.add(node)
            for n in node.neighbors:
                dfs(n)
        self.visited = set()
        self.nodes = list()
        dfs(node)
        print(' -> '.join(self.nodes))
    def traverseBFS(self, node):
        def bfs(node):
            if node in self.visited:
                return
            self.dq.append(node)
            self.visited.add(node)
            #print(f'Initial node => {node.val}')
            while self.dq:
                #print(f'\tdq = {self.dq}')
                size = len(self.dq)
                for i in range(size):
                    #cur = self.dq[0]
                    cur = self.dq.popleft()
                    #print(f'Visiting => {cur.val}')
                    self.nodes.append(str(cur.val))
                    for n in cur.neighbors:
                        if n not in self.visited:
                            self.dq.append(n)
                            self.visited.add(n)
                    #self.dq.popleft()
        self.visited = set()
        self.dq = deque()
        self.nodes = list()
        bfs(node)
        print(' -> '.join(self.nodes))
    def cloneGraph(self, node):
        def dfs(node):
            mapping[node] = Node(node.val)
            for n in node.neighbors:
                if n not in mapping:
                    dfs(n)
                mapping[node].neighbors += [mapping[n]]
        if not node:
            return node
        mapping = dict()
        dfs(node)
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(mapping)
        for k, v in mapping.items():
            print(f'types(k, v) = ({type(k)}, {type(v)}) ; values(k, v) = {k.val}, {v.val}')
            k.print()
            print('~~~~~')
        return mapping[node]

for adj in [
              [[2,4],[1,3],[2,4],[1,3]],
              [[2,3],[1,5],[1,4],[3,5],[2,4,6,7],[5,8],[5,8],[6,7,9],[8]],
              [[2,3],[4,5],[6,7],[8,9],[],[10],[11,12]],
           ]:
    print(f'adj = {adj}')
    sol = Solution()
    g = sol.createGraph(adj)
    print(f'Root node = {g}')
    print('==> DFS')
    sol.traverseDFS(g)
    print('==> BFS')
    sol.traverseBFS(g)
    # a = sol.createAdjList(g)
    # print(f'AdjList from graph = {a}')
    # print('=====> NOW RECREATE THE GRAPH FROM ADJLIST AND TRAVERSE IT <=====')
    # g1 = sol.createGraph(a)
    # print(f'Root node = {g1}')
    # print('==> DFS')
    # sol.traverseDFS(g1)
    # print('==> BFS')
    # sol.traverseBFS(g1)
    # print('=====> NOW CLONE THE GRAPH FROM PREVIOUS GRAPH AND TRAVERSE IT <=====')
    # g2 = sol.cloneGraphOrig(g1)
    # print(f'Root node = {g2}')
    # print('==> DFS')
    # sol.traverseDFS(g2)
    # print('==> BFS')
    # sol.traverseBFS(g2)
    print('=====> NOW CLONE THE GRAPH USING NEW FUNCTION AND TRAVERSE IT <=====')
    g3 = sol.cloneGraph(g)
    print(f'Root node = {g3}')
    print('==> DFS')
    sol.traverseDFS(g3)
    print('==> BFS')
    sol.traverseBFS(g3)
    print('===============================================================')

