from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(node, dest, value):
            if node == dest:
                self.ans = value
                return
            for next_node, next_value in hsh[node]:
                if next_node not in self.seen:
                    self.seen.add(next_node)
                    dfs(next_node, dest, value * next_value)
        
        hsh = defaultdict(list)
        for (n, d), v in zip(equations, values):
            hsh[n] += [[d, v]]
            hsh[d] += [[n, 1/v]]
        res = list()
        for u, v in queries:
            if u not in hsh or v not in hsh:
                res += [-1]
            elif u == v:
                res += [1]
            else:
                self.ans = None
                self.seen = set()
                self.seen.add(u)
                dfs(u, v, 1)
                res += [-1 if self.ans is None else self.ans]
        return res

# Main section
for equations, values, queries in [
            ([['a','b'],['b','c']], [2.0,3.0], [['a','c'],['b','a'],['a','e'],['a','a'],['x','x']]),
            ([['a','b'],['b','c'],['bc','cd']], [1.5,2.5,5.0], [['a','c'],['c','b'],['bc','cd'],['cd','bc']]),
            ([['a','b']], [0.5], [['a','b'],['b','a'],['a','c'],['x','y']]),
            ([['a','b'],['c','d']], [1.0,1.0], [['a','c'],['b','d'],['b','a'],['d','c']]),
            ([['a','b'],['c','d']], [1.0,1.0], [['a','c'],['b','d'],['b','a'],['d','c']]),
            ([['x1','x2'],['x2','x3'],['x3','x4'],['x4','x5']], [3.0,4.0,5.0,6.0], [['x1','x5'],['x5','x2'],['x2','x4'],['x2','x2'],['x2','x9'],['x9','x9']]),
            ([['a','b'],['c','d']], [1.0,1.0], [['a','c'],['b','d'],['b','a'],['d','c']]),
            ([['a','e'],['b','e']], [4.0,3.0], [['a','b'],['e','e'],['x','x']]),
        ]:
    print(f'equations, values, queries = {equations}, {values}, {queries}')
    sol = Solution()
    r = sol.calcEquation(equations, values, queries)
    print(f'r = {r}')
    print('===================')



